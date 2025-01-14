package config

import (
	"log/slog"
	"math/rand"
	"os"

	"github.com/joho/godotenv"
	"github.com/lmittmann/tint"
	"github.com/mattn/go-colorable"
	"github.com/mattn/go-isatty"
)

type configuration struct {
	AppEnvironment string
	BotPrefix       string
	BotStatus 		string
	DiscordToken    string
}

const APP_ENVIRONMENT_LOCAL = "LOCAL"
const APP_ENVIRONMENT_PRODUCTION = "PRODUCTION"
const APP_ENVIRONMENT_DEVELOPMENT = "DEVELOPMENT"

var config *configuration;
var Printer = slog.New(
	tint.NewHandler(
		colorable.NewColorable(os.Stderr),
		&tint.Options{
			NoColor: !isatty.IsTerminal(os.Stderr.Fd()),
		},
	),
)
var tips = []string {
	"Did you know that cake is based on SCP-871 :D",
	"Everything is worth the journey :D",
	"\"Beebo is femboy\" - RelevantCoffee",
	"Did you know that ace is a giraffe?",
	"Beatrix -> Beetroot",
	"Bretzrarei had a great fall in Scp106",
	"No wait! You cannot say the n word-",
	"Day after day, another ddos ensues",
	"Made in Indonesia",
	"Our staff member have a rather fond of their, *anime girls*.",
}

func Load() {
	err := godotenv.Load()
	if err != nil {
		Printer.Error("failed to load environment")
	}

	config = &configuration{
		AppEnvironment: 	os.Getenv("APP_ENVIRONMENT"),
		BotPrefix: 			os.Getenv("BOT_PREFIX"),
		BotStatus: 			os.Getenv("BOT_STATUS"),
		DiscordToken: 		os.Getenv("DISCORD_TOKEN"),
	}
}

func GetAppEnvironment() string {
	return config.AppEnvironment
}

func IsAppEnvironments(environments ...string) bool {
	if len(environments) == 0 {
		return config.AppEnvironment == environments[0]
	}

	for _, environment := range environments {
		if config.AppEnvironment == environment {
			return true
		}
	}

	return false
}

func GetPrefix() string {
	return config.BotPrefix
}

func GetDiscordToken() string {
	return config.DiscordToken
}

func GetMessageTip() string {
	return tips[rand.Intn(len(tips))]
}