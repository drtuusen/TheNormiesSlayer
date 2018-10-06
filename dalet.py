import discord
import asyncio
import time
import math
        
client = discord.Client()

aleph=[]


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
        
@client.event
async def on_member_join(member):
    a = client.get_channel("491320691031932928")
    b = client.get_server("296384240331784212")
    role = discord.utils.get(b.roles, name="Jeunes Ames Vierges")
    await client.add_roles(member, role)
    await client.send_message(a, "Salam, "+ "<@" + member.id + ">."+ "(ID:" + member.id + ") " + " Tu dois accepter les conditions d'utilisation de ce serveur pour continuer ! Pour ce faire tu dois écrire << Je confirme avoir pris connaissance des conditions d'utilisation et de confidentialité, je les accepte et m'engage à les respecter.>>  (Copie colle le c'est bien mieux xd)" + " https://imgur.com/a/HdTDUHl")
    
@client.event
async def on_message(message):
    zb = client.get_channel("491317478178422784")
    b = client.get_server("296384240331784212")
    role = discord.utils.get(b.roles, name="Jeunes Ames Vierges")
    zeta=discord.utils.get(b.roles, name="Théoriciens Du Grand Zbeul")
    teta=discord.utils.get(b.roles, name="Grand philosophe des égouts")
    new = discord.utils.get(b.roles, name="Déchets Confirmés")
    if "Je confirme avoir pris connaissance des conditions d'utilisation et de confidentialité, je les accepte et m'engage à les respecter" in message.content and message.author.id!="491274495986761729" and role in message.author.roles:
        await client.send_message(message.channel, "<@" + message.author.id + ">" + "(ID:" + message.author.id + ") " +"Inscription validée le: " + time.strftime("%A %d %B %Y %H:%M:%S"))
        await client.remove_roles(message.author, role)
        await client.add_roles(message.author, new)
        await client.send_message(zb, "@everyone, dites coucou à " + "<@" + message.author.id + ">. " + "Il vient de rejoindre le niveau -7 de l'enfer !") 
    if message.content[0:5]=="!time" and ((teta in message.author.roles) or (zeta in message.author.roles)):
        po=message.content[6:len(message.content)]
        await client.send_message(message.channel, "<@"+ po + ">" + " Doit accepter les condtions sous 3 jours sous peine de ban.")
        aleph.append([po,time.time()])
    if message.content=="!check" and ((teta in message.author.roles) or (zeta in message.author.roles)):
        for k in aleph:
            ixde=b.get_member(k[0])
            if (time.time() >= k[1] + 17000) and (role in ixde.roles):
                await client.send_message(message.channel, "<@"+k[0]+">" + " (A été Kick).")
                await client.ban(ixde)
            else:
                caca= k[1] + 17000 - time.time()
                caca= caca/3600
                caca1=math.floor(caca)
                caca= round(caca,3)
                min=math.floor((caca-caca1)*60)
                caca = str(caca1)
                min=str(min)
                await client.send_message(message.channel, "<@"+k[0]+">" + " " +  caca + " h et " + min +" mins.")
        await client.send_message(message.channel, "Check terminer.")
    if message.content[0:4]=="!ban":
        mem=b.get_member(message.content[5:len(message.content)])
        await client.send_message(mem, "U got banned: "+"http://moe-desu.com/Original/Images/Error.jpg")
        
        
        
        
                
client.run("NDkxMjc0NDk1OTg2NzYxNzI5.DoFmdw.XRUyZ4BiEQpFZBtY9PoR2MxF0-c")
