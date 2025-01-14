package commands

import (
	"cake/helper/internal/config"
	"cake/helper/internal/discord"
	"fmt"
	"runtime"
	"time"

	"github.com/bwmarrin/discordgo"
)

func AppInfo(s *discordgo.Session, m *discordgo.MessageCreate) {
	builder := discord.NewEmbed().
		SetColor(0x04fb99).
		SetAuthor("thiz waht cake said :3", m.Author.AvatarURL("1024")).
		SetThumbnail(s.State.User.AvatarURL("2048")).
		AddField("Runtime", fmt.Sprintf("Golang [%s]", runtime.Version())).
		AddField("API Version", fmt.Sprint("V", s.State.Ready.Version)).
		SetFooter(config.GetMessageTip()).
		SetTimestamp(time.Now())

	s.ChannelMessageSendEmbedReply(m.ChannelID, builder.MessageEmbed, m.Reference())
}