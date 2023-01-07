# slack2python
a python wrapper of slack bolt

## Usage

```python
import slack2python
from slack_bolt import App

def on_message(event):
    if event.get("text", "") == "init":
        return

        channel = slack2python.Channel.fetch(channel_name="general")
        channel.post("hello world")

        me = Member.fetch("put my member id to here")
        channel.post(f"{me.mention} created this app")
    elif event.get("text", "") == "hello":
        channel = Channel.fetch_by_response(event)
        channel.post("nice to meet you")

def invite_all(ack, body):
    ack()

    channel = Channel.fetch(channel_id=body["channel_id"])
    all_workspace_members = set(Member.fetch_all().values())
    in_channel_members = set(channel.members)

    inviting_members = list(all_workspace_members - in_channel_members)

    if len(inviting_members) > 0:
        channel.invite(inviting_members)
    else:
        channel.post(f"all {len(all_workspace_members)} are in this channel")

app = App(
    token=os.environ.get("SLACK_BOT_USER_OAUTH_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
    )

slack2python.set_app(app)

app.command("/invites")(invite_all)
app.event("message")(on_message)

app.start(port=int(os.environ.get("PORT", 8000)))

```

## Install

```
pip install slack2python
```

## Documentation

Please read [this page](https://2lu3.github.io/slack2python/slack2python.html)
