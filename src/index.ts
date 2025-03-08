import {
    APIInteraction,
    InteractionType,
} from 'discord-api-types/v10'
import { Hono } from 'hono'
import { sign } from 'tweetnacl'
import { Methods } from './methods'

const PUBLIC_KEY = ''
const app = new Hono()

function verifySignature(
    body: string,
    signature: string,
    timestamp: string
) {
    return sign.detached.verify(
        Buffer.from(timestamp + body),
        Buffer.from(signature, 'hex'),
        Buffer.from(PUBLIC_KEY, 'hex')
    )
}

/* Main */
app.post('/', async (context) => {
    try {
        // Verifying secrets
        const signature = context.req.header('X-Signature-Ed25519')!
        const timestamp = context.req.header('X-Signature-Timestamp')!
        const body = await context.req.text()!

        verifySignature(body, signature, timestamp)

        // Parsing request data
        const data = await context.req.json<APIInteraction>()

        // Check if the request was a Ping request
        switch (data.type) {
            case InteractionType.Ping: return context.json({ type: InteractionType.Ping }, 200);
            case InteractionType.ApplicationCommand:
                Methods.InteractionCommmand(data)
                return;
            case InteractionType.MessageComponent:
                return;
            case InteractionType.ModalSubmit:
                return;
        }
    } catch {
        return context.text('invalid request signature', 401)
    }
})