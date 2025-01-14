package bot

import (
	"os"
	"os/signal"
	"syscall"

	"cake/helper/internal/config"
	"cake/helper/internal/discord"
	"cake/helper/internal/handlers"
)

func Start() {
	config.Load()
	discord.InitSession()
	discord.Session.AddHandlerOnce(handlers.ReadyHandler)
	discord.Session.AddHandler(handlers.MessageCreate)
	discord.InitConnection()
	
	defer discord.Session.Close()

	sc := make(chan os.Signal, 1)
	signal.Notify(sc, syscall.SIGINT, syscall.SIGTERM, os.Interrupt, os.Kill)
	<-sc
}