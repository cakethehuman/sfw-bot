package commands

import (
	"cake/helper/internal/api"
	"cake/helper/internal/config"
	"cake/helper/internal/discord"
	"fmt"
	"time"

	"strings"
	"unicode/utf8"

	"github.com/bwmarrin/discordgo"
)

// https://stackoverflow.com/questions/55036156/how-to-replace-all-html-tag-with-empty-string-in-golang

const (
    htmlTagStart = 60 // Unicode `<`
    htmlTagEnd   = 62 // Unicode `>`
)

// Aggressively strips HTML tags from a string.
// It will only keep anything between `>` and `<`.
func stripHtmlTags(s string) string {
    // Setup a string builder and allocate enough memory for the new string.
    var builder strings.Builder
    builder.Grow(len(s) + utf8.UTFMax)

    in := false // True if we are inside an HTML tag.
    start := 0  // The index of the previous start tag character `<`
    end := 0    // The index of the previous end tag character `>`

    for i, c := range s {
        // If this is the last character and we are not in an HTML tag, save it.
        if (i+1) == len(s) && end >= start {
            builder.WriteString(s[end:])
        }

        // Keep going if the character is not `<` or `>`
        if c != htmlTagStart && c != htmlTagEnd {
            continue
        }

        if c == htmlTagStart {
            // Only update the start if we are not in a tag.
            // This make sure we strip out `<<br>` not just `<br>`
            if !in {
                start = i

                // Write the valid string between the close and start of the two tags.
                builder.WriteString(s[end:start])
            }
            in = true
            continue
        }
        // else c == htmlTagEnd
        in = false
        end = i + 1
    }
    s = builder.String()
    return s
}


func ServerCommand(s *discordgo.Session, m *discordgo.MessageCreate) {
	builder := discord.NewEmbed().
		SetColor(0x0000fb).
		SetAuthor("Waiting for api.scplist.kr", s.State.User.AvatarURL("1024")).
		SetFooter(config.GetMessageTip()).
		SetTimestamp(time.Now())

	m2, err := s.ChannelMessageSendEmbed(m.ChannelID, builder.MessageEmbed)
	if err != nil {
		config.Printer.Error("unable to send server command", "error", err)
		return
	}

	res, err := api.Search(&api.SortOption{
		Search: "SFW",
		Sort: "PLAYERS_DESC",
		CountryFilter: []string { "SG" },
		HideEmptyServer: false,
		HideFullServer: false,
		Modded: nil,
		FriendlyFire: nil,
		Whitelist: nil,
	})

	if err != nil {
		builder.
			SetColor(0xfb0000). 
			SetAuthor("cake expewienced ewwow (>~<)", m.Author.AvatarURL("1024")).
			SetThumbnail(s.State.Ready.User.AvatarURL("2048")).
			SetDescription("an ewwow happenyed when twying t-to retwieve list"). 
			SetFooter(fmt.Sprintf("Requested by %s", m.Author.Username)). 
			SetTimestamp(time.Now())

		s.ChannelMessageEditEmbed(m2.ChannelID, m2.ID, builder.MessageEmbed)
		return
	}

	for _, server := range res.Servers {
		builder.AddField(
			stripHtmlTags(server.Info),
			fmt.Sprintf(
				"Registrar Id: %d\nGame Version: %s\nPlayers Count: %s",
				server.ServerId,
				server.Version,
				server.Players,
			),
		)
	}

	builder.
		SetColor(0x04fb99).
		SetAuthor("this is what cake said :3", m.Author.AvatarURL("1024")).
		SetThumbnail(s.State.User.AvatarURL("2048")).
		SetFooter(config.GetMessageTip()). 
		SetTimestamp(time.Now())
	
	s.ChannelMessageEditEmbed(m2.ChannelID, m2.ID, builder.MessageEmbed)
}