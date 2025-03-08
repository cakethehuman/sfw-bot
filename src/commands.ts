import { SlashCommandBuilder } from "@discordjs/builders";
import { APIApplicationCommandInteraction } from "discord-api-types/v10";

export const Commands = [
    {
        data: new SlashCommandBuilder()
        .setName('servers')
        .setDescription('Displays the player count for SFW game servers'),
        async execute(interaction: APIApplicationCommandInteraction) {

        }
    }
]