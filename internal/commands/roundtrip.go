package commands

import (
	"cake/helper/internal/config"
	"cake/helper/internal/discord"
	"fmt"
	"time"

	"github.com/bwmarrin/discordgo"
)

func Roundtrip(s *discordgo.Session, m *discordgo.MessageCreate) {
	builder := discord.NewEmbed().
		SetColor(0x04f0af).
		SetAuthor("[Golang] Calculating Roundtrip")

	startTimestamp := time.Now().UnixMilli()
	m2, err := s.ChannelMessageSendEmbed(m.ChannelID, builder.MessageEmbed)

	if err != nil {
		config.Printer.Error("Error at roundtrip message command", "error", err)
		return
	}

	roundtripMs := time.Now().UnixMilli() - startTimestamp
	builder.
		SetColor(0x04fb99).
		SetAuthor("[Golang] Roundtrip Successfull", m.Author.AvatarURL("1024")).
		SetDescription(
			fmt.Sprintf("Roundtrip: %dms\nGateway: %dms", roundtripMs, s.HeartbeatLatency().Milliseconds()),
		).
		SetThumbnail(s.State.User.AvatarURL("2048")).
		SetFooter(config.GetMessageTip()).
		SetTimestamp(time.Now())

	s.ChannelMessageEditEmbed(m2.ChannelID, m2.ID, builder.MessageEmbed)
}