package handlers

import (
	"context"
	"log/slog"
	"cake/helper/internal/config"

	"github.com/bwmarrin/discordgo"
)

func ReadyHandler(s *discordgo.Session, r *discordgo.Ready) {
	config.Printer.LogAttrs(
		context.Background(),
		slog.LevelInfo,
		"Client is ready with identity",
		slog.Int("Version", r.Version),
		slog.String("SessionID", r.SessionID),
		slog.String("User", r.User.Username),
	)
}