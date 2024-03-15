import discord, os;
from discord.ext import commands
intents = discord.Intents.default();
intents.message_content = True;
bot = discord.Client(intents = intents);

@bot.event
async def on_ready():
    print(f'Started bot {bot.user}');
    playing = discord.Game("upload file to obfuscate");
    await bot.change_presence(activity=playing)

current_session_id = 0;

@bot.event
async def on_message(msg):
    author = msg.author;
    if author == bot.user: return;
    channel = msg.channel;
    content = msg.content;

    if content == msg.attachments: return;

    attachments = msg.attachments;
    if len(attachments) != 1:
        return await channel.send("Expected exactly one attachment.");
    attachmentone = attachments[0];
    filename = attachmentone.filename;
    if not (filename.endswith(".lua") or filename.endswith(".txt")):
        return await channel.send("Expected a .lua or .txt file.");
    
    global current_session_id;
    current_session_id += 1;
    session_id = current_session_id;

    inputfile = None;
    inputfilename = f"sessionIN{session_id}.lua";
    outputfilename = f"sessionOUT{session_id}.lua";

    content = await attachmentone.read();
    inputfile = open(inputfilename, "wb");
    if inputfile:
        inputfile.write(content);
        

        os.system(f"lua 'src/cli.lua' {inputfilename} --out {outputfilename} --preset Medium");
        

        await channel.send("Here is your file! ", file = discord.File(open(outputfilename, "rb"), filename = f"RinXSibidi{session_id}.lua"));

        os.system(f"rm -f {outputfilename}");



bot.run(os.environ["bot_token"]);
