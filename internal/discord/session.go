package discord;

import (
	"github.com/bwmarrin/discordgo"

	"cake/helper/internal/config"
)

var Session *discordgo.Session;

func InitSession() {
	var err error;
	Session, err = discordgo.New("Bot " + config.GetDiscordToken())

	if err != nil {
		config.Printer.Error("failed to initialize discord session", "error", err)
	}

	Session.Identify.Intents = 
		discordgo.IntentGuildMembers |
		discordgo.IntentGuildMessages |
		discordgo.IntentMessageContent
}

func InitConnection() {
	if err := Session.Open(); err != nil {
		config.Printer.Error("failed to open session connection", "error", err)
	}
}