package main

import (
	_ "flag"
	"fmt"
	"log"
	"os"
	"os/signal"
	"time"

	"github.com/bwmarrin/discordgo"
	"github.com/joho/godotenv"
)

var (
	Token    string
	Prefix   string
	GuildID  string
	Instance Framework
	Cache ServerSummaryResponse
	ServerNames map[int32]string = map[int32]string {
		72115: "Vanilla Dreams", 
		72116: "Yummy Dreams", 
		72117: "Eggzellent Dreams",
	}
)

func init() {
	godotenv.Load()

	Token = os.Getenv("TOKEN")
	Prefix = os.Getenv("PREFIX")
	GuildID = os.Getenv("GUILD_ID")
	// flag.StringVar(&Token, "Token", "", "Discord Authentication Token")
	// flag.StringVar(&Prefix, "Prefix", "$", "Prefix for Discord commands")
	// flag.Parse()
}

func main() {
	Instance = Framework {
		Prefix: Prefix,
	};

	go heartbeat();
	Cache = Instance.GetServerSummaries()

	discord, err := discordgo.New(fmt.Sprintf("Bot %s", Token))
	checkNilErr(err)

	discord.Identify.Intents = discordgo.IntentsAllWithoutPrivileged |
		discordgo.IntentMessageContent

	discord.AddHandlerOnce(Instance.Ready)
	discord.AddHandler(Instance.MessageCreate)
	discord.AddHandler(Instance.InteractionCreate)

	err = discord.Open()
	checkNilErr(err)

	_commands, err := discord.ApplicationCommands(discord.State.User.ID, GuildID)
	checkNilErr(err)

	for i, v := range _commands {
		discord.ApplicationCommandDelete(v.ApplicationID, GuildID, v.ID)
		_commands[i] = nil
	}

	registeredCommands := make([]*discordgo.ApplicationCommand, len(Commands))

	for i, v := range Commands {
		cmd, err := discord.ApplicationCommandCreate(discord.State.User.ID, GuildID, v)
		checkNilErr(err)
		registeredCommands[i] = cmd
	}

	defer discord.Close()

	// fmt.Println("Preventing program from exitting")
	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt)
	<-c
}

func heartbeat() {
	for range time.Tick(time.Second * 30) {
		log.Print("Hit 30 seconds mark, Updating server summaries..")
		Cache = Instance.GetServerSummaries()
	}
}

func checkNilErr(e error) {
	if e != nil {
		log.Panic(e)
	}
}