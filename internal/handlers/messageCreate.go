package handlers

import (
	"strings"
	"cake/helper/internal/discord"
	"cake/helper/internal/commands"

	"github.com/bwmarrin/discordgo"
)

func MessageCreate(s *discordgo.Session, m *discordgo.MessageCreate) {
	if m.Author.Bot == true {
		return
	}

	command, _ := discord.ParseContent(m)

	if command == "" {
		return
	}

	switch (strings.ToLower(command)) {
	case "ping":
		commands.Roundtrip(s, m)
	case "roundtrip":
		commands.Roundtrip(s, m)
	case "info":
		commands.AppInfo(s, m)
	case "server":
		commands.ServerCommand(s, m)
	case "servers":
		commands.ServerCommand(s, m)
	}
}