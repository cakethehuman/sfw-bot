import { APIApplicationCommandInteraction } from "discord-api-types/v10"
import { Commands } from "./commands"

export const Methods = {
    'InteractionCommmand': async(interaction: APIApplicationCommandInteraction) => {
        const command = Commands.find(x => x.data.name === interaction.data.name)
        
        if (command) {
            command.execute(interaction)
        }
    }
}