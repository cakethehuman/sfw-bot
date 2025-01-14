package discord

import (
	"cake/helper/internal/config"
	"strings"

	"github.com/bwmarrin/discordgo"
)

func RegisterCommandsForGuild(guild *discordgo.Guild, session *discordgo.Session) {

}

func ParseContent(m *discordgo.MessageCreate) (command string, content string) {
	i := strings.Index(m.Content, config.GetPrefix())
	if i != 0 {
		return
	}

	content = m.Content[(i + 1):]
	i = strings.Index(m.Content, " ")
	if i == -1 {
		i = len(content) + 1
	}

	command = content[0:(i - 1)]
	return
}

