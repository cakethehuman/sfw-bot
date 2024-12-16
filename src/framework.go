package main

import (
	"bytes"
	"encoding/json"
	"math/rand"
	"net/http"
	"strings"
	"time"

	"github.com/bwmarrin/discordgo"
)

var (
	SCPSLAPI string = "https://api.scplist.kr/api/servers"
	RandomTipMessages = []string {
		"Cake is based on SCP-871 :D",
		"Everything is worth the journey :D",
		"\"Beebo is femboy\" - RelevantCoffee",
		"Did you know that ace is a giraffe?",
		"Beatrix -> Beetroot",
		"Bretzrarei had a great fall in Scp106",
		"No wait! You cannot say the n word-",
		"Day after day, another ddos ensues",
	}
)

type Framework struct {
	Prefix string
}

func (framework Framework) GetPrefix() string {
	return framework.Prefix
}

func (framework Framework) IsAllowed(m *discordgo.MessageCreate) bool {
	if m.Author.Bot {
		return false
	}

	if !strings.HasPrefix(m.Content, Prefix) {
		return false
	}

	return true
}

func (framework Framework) ParseContent(m *discordgo.MessageCreate) (command string, content string) {
	i := strings.Index(m.Content, framework.GetPrefix())
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

type ServerSummary struct {
	AccountId int64 `json:"accountId"`
	ServerId int64 `json:"serverId"`
	Ip string `json:"ip"`
	Port int32 `json:"port"`
	Online bool `json:"online"`
	Version string `json:"version"`
	FriendlyFire bool `json:"friendlyFire"`
	Modded bool `json:"modded"`
	Whitelist bool `json:"whitelist"`
	IsoCode string `json:"isoCode"`
	Info string `json:"info"`
	Pastebin string `json:"pastebin"`
	Official int32 `json:"official"`
	Distance float32 `json:"distance"`
	TechList []*ServerTech `json:"techList"`
	Players string `json:"players"`
}

type ServerTech struct {
	Id int64 `json:"id"`
	Name string `json:"name"`
	Version string `json:"version"`
}

type ServerSortOption struct {
	Search string `json:"search"`
	CountryFilter []string `json:"countryFilter"`
	HideEmptyServer bool `json:"hideEmptyServer"`
	HideFullServer bool `json:"hideFullServer"`
	FriendlyFire *bool `json:"friendlyFire"`
	Whitelist *bool `json:"whitelist"`
	Modded *bool `json:"modded"`
	Sort string `json:"sort"`
}

type ServerSummaryResponse struct {
	OnlineUserCount int32 `json:"onlineUserCount"`
	OnlineServerCount int32 `json:"onlineServerCount"`
	DisplayUserCount int32 `json:"displayUserCount"`
	DisplayServerCount int32 `json:"displayServerCount"`
	OfflineServerCount int32 `json:"offlineServerCount"`
	Servers []*ServerSummary `json:"servers"`
}

func (framework Framework) GetServerSummaries() ServerSummaryResponse {
	r, err := json.Marshal(ServerSortOption {
		Search: "SFW",
		Sort: "PLAYERS_DESC",
		CountryFilter: []string {"SG"},
		HideEmptyServer: false,
		HideFullServer: false,
		Modded: nil,
		FriendlyFire: nil,
		Whitelist: nil,
	})
	checkNilErr(err)

	response, err := http.Post(SCPSLAPI, "application/json", bytes.NewBuffer(r))
	checkNilErr(err)

	var s ServerSummaryResponse

	decoder := json.NewDecoder(response.Body)
	err = decoder.Decode(&s)
	checkNilErr(err)

	return s
}

func (framework Framework) GetRandomTip() string{
	random := rand.New(rand.NewSource(time.Now().Unix()))
	return RandomTipMessages[random.Intn(len(RandomTipMessages))]
}