package main

import (
	"log"

	"github.com/bwmarrin/discordgo"
)

func (x Framework) Ready(s *discordgo.Session, r *discordgo.Ready) {
	log.Printf("Ready on %s", r.User.Username)
}

func (framework Framework) MessageCreate(s *discordgo.Session, m *discordgo.MessageCreate) {
	if !(framework.IsAllowed(m)) {
		return
	}
	
	command, _ := framework.ParseContent(m)
	if h, ok := MessageHandlers[command]; ok {
		h(s, m)
	}
}

func (framework Framework) InteractionCreate(s *discordgo.Session, i *discordgo.InteractionCreate) {
	if i.Type == discordgo.InteractionApplicationCommand {
		if h, ok := Handlers[i.ApplicationCommandData().Name]; ok {
			// s.InteractionRespond(i.Interaction, &discordgo.InteractionResponse{
			// 	Type: discordgo.InteractionResponseDeferredChannelMessageWithSource,
			// })

			h(s, i)
		}
		return
	}
}