from pyrogram import Client, filters, idle

app = Client("DeleteGroupJoinMessage_bot",
             bot_token = "1863735388:AAHNAnQmal5sigP1-rMkiQ_--Q6qR7W6k3M"

             )

@app.on_message(filters.group)
def delete_unwanted_message(client, message):
    unwanted_messages = [
        message.new_chat_members,
        message.left_chat_member,
        message.new_chat_title,
    ]
    for unwanted in unwanted_messages:
        if unwanted is not None:
            client.delete_messages(message.chat.id, [message.message_id])

    if message.text is not None and message.text.find("https://t.me/joinchat/") > -1:
        member = client.get_chat_member(message.chat.id, message.from_user.id)
        if not (member.status == "creator" or member.status == "administrator"):
            client.delete_messages(message.chat.id, [message.message_id])  # Delete none admin invitation


app.start()
idle()