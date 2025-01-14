package api

import (
	"bytes"
	"cake/helper/internal/config"
	"encoding/json"
	"net/http"
	"time"
)

type server struct {
	AccountId    int64   `json:"accountId"`
	ServerId     int64   `json:"serverId"`
	Ip           string  `json:"ip"`
	Port         int32   `json:"port"`
	Online       bool    `json:"online"`
	Version      string  `json:"version"`
	FriendlyFire bool    `json:"friendlyFire"`
	Modded       bool    `json:"modded"`
	Whitelist    bool    `json:"whitelist"`
	IsoCode      string  `json:"isoCode"`
	Info         string  `json:"info"`
	Pastebin     string  `json:"pastebin"`
	Official     int32   `json:"official"`
	Distance     float32 `json:"distance"`
	TechList     []*tech `json:"techList"`
	Players      string  `json:"players"`
}

type tech struct {
	Id      int64  `json:"id"`
	Name    string `json:"name"`
	Version string `json:"version"`
}

type SortOption struct {
	Search          string   `json:"search"`
	CountryFilter   []string `json:"countryFilter"`
	HideEmptyServer bool     `json:"hideEmptyServer"`
	HideFullServer  bool     `json:"hideFullServer"`
	FriendlyFire    *bool    `json:"friendlyFire"`
	Whitelist       *bool    `json:"whitelist"`
	Modded          *bool    `json:"modded"`
	Sort            string   `json:"sort"`
}

type response struct {
	OnlineUserCount    int32     `json:"onlineUserCount"`
	OnlineServerCount  int32     `json:"onlineServerCount"`
	DisplayUserCount   int32     `json:"displayUserCount"`
	DisplayServerCount int32     `json:"displayServerCount"`
	OfflineServerCount int32     `json:"offlineServerCount"`
	Servers            []*server `json:"servers"`
}

const url = "https://api.scplist.kr/api/servers"

var (
	cache		response
	lastFetch 	time.Time
)


func Search(option *SortOption) (response response, err error) {
	if time.Now().Before(lastFetch.Add(60 * time.Second)) {
		response = cache
		return
	}

	r, err := json.Marshal(option)
	res, err := http.Post(url, "application/json", bytes.NewBuffer(r))
	if err != nil {
		config.Printer.Error("error while trying to search scp summaries", "error", err)
	}

	err = json.NewDecoder(res.Body).Decode(&cache)
	if err != nil {
		config.Printer.Error("unable to decode search response", "error", err)
	}
	
	response = cache
	return
}