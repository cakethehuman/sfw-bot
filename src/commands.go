package main

import (
	"fmt"
	"time"

	"github.com/bwmarrin/discordgo"
)

var (
	Commands = []*discordgo.ApplicationCommand {
		{
			Name: "servers",
			Description: "Get a summary of SFW Server's playercounts",
			// Options: []*discordgo.ApplicationCommandOption {
			// 	{
			// 		Name: "Game",
			// 		Type: discordgo.ApplicationCommandOptionString,
			// 		Required: false,
			// 		Choices: []*discordgo.ApplicationCommandOptionChoice {
			// 			{
			// 				Name: "SCP: Secret Laboratory",
			// 				Value: "scpsl",
			// 			},
			// 			{
			// 				Name: "Battlebit Remastered",
			// 				Value: "battlebit",
			// 			},
			// 		},
			// 	},
			// },
		},
		{
			Name: "info",
			Description: "A brief information about CakeHelper :3",
		},
	}
	Handlers = map[string]InteractionHandler {
		"servers": func (s *discordgo.Session, i *discordgo.InteractionCreate) {
			description := ""

			for _, server := range Cache.Servers {
				description += fmt.Sprintf("**%s** (%d)\nGame Version: **%s**\nPlayer Counts: **%s**\n\n", ServerNames[int32(server.ServerId)], server.ServerId, server.Version, server.Players)
			}

			// embed := &discordgo.MessageEmbed {
			// 	Author: &discordgo.MessageEmbedAuthor{
			// 		Name: "[Go] this is what cake said :3",
			// 		IconURL: s.State.User.AvatarURL("2048"),
			// 	},
			// 	Color: 0x04fb99,
			// 	Description: description,
			// 	Timestamp: ,
			// }

			embed := NewEmbed().
				SetColor(0x04fb99).
				SetDescription(description).
				SetAuthor("[Go] this is waht cake said :3", s.State.User.AvatarURL("2048")).
				SetFooter(Instance.GetRandomTip())

			embed.Timestamp = time.Now().Format("2006-01-02T15:04:05-07:00")
			
			s.InteractionRespond(i.Interaction, &discordgo.InteractionResponse{
				Type: discordgo.InteractionResponseChannelMessageWithSource,
				Data: &discordgo.InteractionResponseData{
					Embeds: []*discordgo.MessageEmbed {embed.MessageEmbed},
				},
			})
		},
	}

	MessageHandlers = map[string]MessageHandler {
		"servers": func(s *discordgo.Session, m *discordgo.MessageCreate) {
			description := ""

			for _, server := range Cache.Servers {
				description += fmt.Sprintf("**%s** (%d)\nGame Version: **%s**\nPlayer Counts: **%s**\n\n", ServerNames[int32(server.ServerId)], server.ServerId, server.Version, server.Players)
			}

			embed := NewEmbed().
				SetColor(0x04fb99).
				SetDescription(description).
				SetAuthor("[Go] this is waht cake said :3", s.State.User.AvatarURL("2048")).
				SetFooter(Instance.GetRandomTip())

			embed.Timestamp = time.Now().Format("2006-01-02T15:04:05-07:00")
			
			s.ChannelMessageSendEmbed(m.ChannelID, embed.MessageEmbed)
		},
	}
)

type InteractionHandler func(s *discordgo.Session, i *discordgo.InteractionCreate)
type MessageHandler func(s *discordgo.Session, m *discordgo.MessageCreate)