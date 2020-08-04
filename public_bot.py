import discord
import asyncio
from asyncio import sleep
from discord.ext import commands
import random, glob

# Setup
bot = commands.Bot(command_prefix=('sudo ', 'Sudo ', 'SUDO ', 'sudo'))
bot.remove_command('help')
embed_colour = discord.Colour.red()
random.seed()

# TODO: Have bot automatically find these based on the server the command is called
shake_room1 = 709974781252075640
shake_room2 = 709974744329486346
access_role = 689296629836415022

gagged = []

@bot.event
async def on_ready():
	print("Running")

# All functionality that checks every sent message.
@bot.event
async def on_message(message):
	if message.author.id in gagged:
		await message.delete()
	await bot.process_commands(message)

	if message.content.upper() == "FUCK":
		await message.channel.send(file=discord.File(open("fuck.mp4", "rb")))

	if message.content.upper() == "SOBBING":
		await message.channel.send(file=discord.File(open("sobbing.png", "rb")))
	
	if message.content.upper() == "PAIN":
		pain_size = len(glob.glob('pain/*'))
		pain = random.uniform(0,pain_size)
		await message.channel.send(file=discord.File(open("pain/{}.png".format(int(pain)), "rb")))


# Basic Utility 

@bot.command()
async def s(ctx):
	
	monkey = bot.get_channel(id1)
	zone = bot.get_channel(id2)
	target = ctx.message.mentions[0]
	ids = (role.id for role in target.roles)

	if ctx.message.mention_everyone or access_role not in ids or not target.voice.self_deaf:
		pass

	else:

		original_channel = target.voice.channel
		await target.send("Wake up <@{}> >:(".format(target.id))
	
		for x in range(4):
			# Moves user back and fourth, muting/deafening each loop
			await target.edit(voice_channel=monkey, deafen=True, mute=True)
			await sleep(0.2)
			await target.edit(voice_channel=zone, deafen=False, mute=False)

		await target.edit(voice_channel=original_channel)

@bot.command()
async def shake(ctx):
	
	monkey = bot.get_channel(id1)
	zone = bot.get_channel(id2)

	target = ctx.message.mentions[0]

	ids = (role.id for role in target.roles)

	if ctx.message.mention_everyone or access_role not in ids or not target.voice.self_deaf:
		pass

	else:

		#current_channel = message.channel
		original_channel = target.voice.channel
		await target.send("Wake up <@{}> >:(".format(target.id))
	
		for x in range(4):

			# Moves user back and fourth, muting/deafening each loop
			await target.edit(voice_channel=monkey, deafen=True, mute=True)
			await sleep(0.2)
			await target.edit(voice_channel=zone, deafen=False, mute=False)

		await target.edit(voice_channel=original_channel)

@bot.command()
async def airstrike(ctx):
	
	monkey = bot.get_channel(id1)
	zone = bot.get_channel(id2)

	target = ctx.message.mentions[0]

	ids = (role.id for role in target.roles)

	if ctx.message.mention_everyone or access_role not in ids or not target.voice.self_deaf:
		pass

	else:

		#current_channel = message.channel
		original_channel = target.voice.channel
	
		for x in range(4):
			await target.send("Wake up <@{}> >:(".format(target.id), file=discord.File(open("blast.jpg", "rb")))
			await target.move_to(channel=monkey)
			await target.move_to(channel=zone)

		await target.move_to(channel=original_channel)

@bot.command()
async def summon(ctx):

	target = ctx.message.mentions[0]

	if ctx.message.mention_everyone:
		pass

	else:
		await ctx.message.channel.send("Pinging")
		#current_channel = message.channel
	
		for x in range(4):
			await target.send("hey <@{}> get in discord".format(target.id), file=discord.File(open("blast.jpg", "rb")))
			# await target.move_to(channel=monkey)
			# await target.move_to(channel=zone)

		# await target.move_to(channel=original_channel)

@bot.command()
async def gag(ctx):

	ids = (role.id for role in ctx.message.mentions[0].roles)
	target = ctx.message.mentions[0]

	if ctx.message.mention_everyone or access_role not in ids or ctx.message.author.id in gagged:
			pass

	else:
		if target.id in gagged:
			await ctx.message.channel.send("{} is already muted.".format(target.display_name))
		else:
			gagged.append(target.id)
			await ctx.message.channel.send("Muted {}.".format(target.display_name))

@bot.command()
async def ungag(ctx):

	ids = (role.id for role in ctx.message.mentions[0].roles)
	target = ctx.message.mentions[0]

	if ctx.message.mention_everyone or access_role not in ids or ctx.message.author.id in gagged:
			pass

	else:
		if target.id in gagged:
			gagged.remove(target.id)
			await ctx.message.channel.send("Unmuted {}.".format(target.display_name))
		else:
			await ctx.message.channel.send("{} isn't muted dumbass.".format(target.display_name))

@bot.command()
async def echo(ctx):

	msg = ctx.message.content[9:]

	if ctx.author.id == 722364047839723561 or msg.upper() == "FUCK":
		pass
	
	else:

		for x in range(5):
			await ctx.message.channel.send(msg)
			await sleep(0.5)

		
@bot.command(aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.author.voice.channel
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f"Joined {channel}")

# WIP. Help command that gives users all the commands and usage
@bot.command()
async def help(ctx):
	embed=discord.Embed(title="Commands ", description="{ } means input required", color=embed_colour)
	embed.add_field(name="sudo shake {@target}", value="sudo get {subject_name} ", inline=True)
	embed.add_field(name="moves target between two channels rapidly", value="im gonna change this dw about it", inline=True)
	embed.add_field(name="sudo year {1,2,68, etc}", value="sudo game {minecraft}", inline=True)
	embed.add_field(name="Assigns a year role. Increments in August", value="Assigns you a game role for @mentions", inline=True)
	embed.add_field(name="sudo FUCK", value="", inline=True)
	embed.add_field(name="FUCK", value="", inline=True)
	await ctx.message.channel.send(embed=embed)

# Dictionary of textbooks/guides related to course	
subjects = {
		"ENPH": "270 - http://93.174.95.29/main/CE1E90DC739863A9788F6324038E2DFB\nThe Bible - http://93.174.95.29/main/05D120938A4D7EBB5A706CE17F66B547",
		"MECH": "260/360 - http://93.174.95.29/main/4B6F6F6DF336EF7DB2219A8E66B1C498\n",
		"ELEC": "nothing here yet, but MNA >> Mesh",
		"PHYS": "250 - http://93.174.95.29/main/318C1507190566EA13AEB003893A7569\n",
		"MATH": "217 - http://www.math.ubc.ca/~CLP/CLP3/ & http://www.math.ubc.ca/~CLP/CLP4/\n255/257 - https://www.jirka.org/diffyqs/diffyqs.pdf\n",
		"CPEN": "https://stackoverflow.com/",
		"APSC": "https://mech2.sites.olt.ubc.ca/files/2014/12/S01_6161.jpg",
		"SPECS": "https://docs.google.com/spreadsheets/d/119mEbyerER02r8lSYzcT4sovFmxW48su0XgUqfFStf0/edit?usp=sharing",
		}

# Allows users to get saved 
@bot.command()
async def get(ctx): 
	request = ctx.message.content.upper()

	if "SPECS" in request:
			embed = discord.Embed(title="Robot Summer component datasheets (WIP):", description=subjects["SPECS"], colour=embed_colour)
			await ctx.message.channel.send(embed=embed)

	elif "ALL" in request:
		for subject in subjects:
			await ctx.message.channel.send("**{} Textbooks:**".format(subject))
			await ctx.message.channel.send(subjects[subject])

	else:		
		for subject in subjects:
			if subject in request:	
				embed = discord.Embed(title="{} Textbooks:".format(subject), description=subjects[subject], colour=embed_colour)
				await ctx.message.channel.send(embed=embed)


# Role Management 


# Sends a welcome message to new members both in general chat and directly
@bot.event
async def on_member_join(member):
	general = bot.get_channel(729877762181169259)
	embed = discord.Embed(
		description = '**Welcome to the Fizz Discord <@{}>!**\n\nAssign yourself a role by typing: ```sudo year <Your Year #>```'.format(member.id),
		colour = embed_colour
	)

	await general.send(embed=embed)
	await member.send(embed=embed)

# Years for role manageament
years = {
	1: "Pre-EngPhys",
	2: "Pre-EngPhys",
	3: "3rd Year",
	4: "4th Year",
	5: "5th Year +",
}

# Years for updating standing
rollover = {
	"Pre-EngPhys": "2nd Year",
	"2nd Year": "3rd Year",
	"3rd Year": "4th Year",
	"4th Year": "5th Year +",
	"5th Year +": "5th Year +"
}

# Game tags for role manageament
games = {
	"LEAGUE": "League of Legends",
	"CS": "CS:GO",
	"MINECRAFT": "Minecraft",
	"SMASH": "Smash",
	"VALORANT": "Valorant"
}

# Allows users to give themselves a year role. Usage: sudo year <1,2,3,4....>
@bot.command()
async def year(ctx):

	year = int(float(ctx.message.content[9:]))

	if year >= 5:
		year = 5

	role = discord.utils.get(ctx.guild.roles, name=years[year])
	role = discord.utils.get(ctx.guild.roles, name=years[year])

	# Adding / removing year role
	if role in ctx.message.author.roles:
		await ctx.message.author.remove_roles(role)
		embed = discord.Embed(description='**You are no longer {}**'.format(years[year]), colour=embed_colour)
		await ctx.message.channel.send(embed=embed)
	else:
		await ctx.message.author.add_roles(role)
		embed = discord.Embed(description='**You are now {}**'.format(years[year]), colour=embed_colour)
		await ctx.message.channel.send(embed=embed)

	# Clear any other year roles (Probably could be handled differently but it is almost 2am rn)
	for role in ctx.message.author.roles:
		if role.name in list(rollover.keys()) and role.name != years[year]:
			await ctx.message.author.remove_roles(role)




# Updates year standing. Only Andrew can use this :)
@bot.command()
async def supersecretcommandname(ctx):

	if ctx.message.author.id == 168388106049814528:
		all_years = list(rollover.keys())
		members = ctx.guild.members
	
		for member in members:
			print(member.roles)
			for role in member.roles:
				if role.name in all_years:
					new_role = discord.utils.get(ctx.guild.roles, name=rollover[role.name])
					old_role = discord.utils.get(ctx.guild.roles, name=role.name)
					print(new_role)
					print(old_role)

					await member.remove_roles(old_role)
					await member.add_roles(new_role)
					break
	else: 
		embed = discord.Embed(description = '**Peasants cannot use this command**', colour = embed_colour)
		await ctx.message.channel.send(embed=embed)


# Allows users to give themselves a game tag. Usage: sudo game <Minecraft, CS, lol>
@bot.command()
async def game(ctx):

	request = str(ctx.message.content[10:]).upper()

	role = discord.utils.get(ctx.guild.roles, name=games[request])
	if role in ctx.message.author.roles:
		await ctx.message.author.remove_roles(role)
		embed = discord.Embed(description = '**You no longer have the {} role**'.format(games[request]), colour = embed_colour)
		await ctx.message.channel.send(embed=embed)
	else:
		await ctx.message.author.add_roles(role)
		embed = discord.Embed(description = '**You were given the {} role**'.format(games[request]), colour = embed_colour)
		await ctx.message.channel.send(embed=embed)

# Discord Bot Token. Don't fucking leak this.
bot.run("hi")


# Regular methods