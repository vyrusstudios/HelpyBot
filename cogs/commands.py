import discord
from discord.ext import commands
import asyncio
import datetime
import re
import sqlite3

class CommandsCog(commands.Cog, discord.Client):

	def __init__(self, client):
		self.bot = client
		db = sqlite3.connect('HelpyBot.db')
		cursor = db.cursor()

	@commands.command()
	async def freddy_info(self, ctx):
		embed = discord.Embed(title="Freddy Fazbear", colour=discord.Colour(0x64053b), description="Freddy Fazbear is the staple character of FNAF AR. He will slowly circle the player getting closer and closer until he either haywires, or he rushes. When he haywires, you have to look away. Do not shock him. When he rushes, he will either run without uncloaking, or he will uncloak and attack you")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/716354692355063818/720716273570414631/alpine_ui_plushsuit_freddy.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on Freddy Fazbear:')
		embed.add_field(name="Rush Attacks", value="When he rushes and he uncloaks, you have to shock him before he disappears, or else you will lose. If he does not decloak, you don’t need to shock him. His AI is the baseline for all characters, so remembering these tactics will help you.")
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def bonnie_info(self, ctx):
		embed = discord.Embed(title="Bonnie the Bunny", colour=discord.Colour(0x64053b), description='Bonnie is one of the original 4 characters. He will slowly circle the player getting closer and closer until he either haywires, or he rushes. When he haywires, you have to look away. Do not shock him. When he rushes, he will either run without uncloaking, or he will uncloak and attack you')
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/716354692355063818/720723349042364487/alpine_ui_plushsuit_bonnie.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on Bonnie the Bunny:')
		embed.add_field(name="Rush Attacks", value="When he rushes and he uncloaks, you have to shock him before he disappears, or else you will lose. If he does not decloak, you don’t need to shock him. His AI is very similar to Freddy’s.")
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def chica_info(self, ctx):
		embed=discord.Embed(title='Chica the Chicken', colour=discord.Colour(0xe7a11c), description='Chica is one of the original 4 characters. She will slowly circle the player getting closer and closer until she either haywires, or she rushes. When she haywires, you have to look away. Do not shock her. When she rushes, she will either run without uncloaking, or she will uncloak and attack you. She also makes chomping noises when walking around.')
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/716354692355063818/720725200278388836/alpine_ui_plushsuit_chica.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on Chica the Chicken:')
		embed.add_field(name="Rush Attacks", value="When she rushes and she uncloaks, you have to shock her before she disappears, or else you will lose. If she does not decloak, you don’t need to shock her. Her AI is very similar to Freddy’s.")
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def foxy_info(self, ctx):
		embed = discord.Embed(title="Foxy the Pirate Fox", colour=discord.Colour(0x64053b), description="Foxy is one of the original 4 characters. Unlike the others he will run around you frequently until he finds an opening for an attack.  He will either haywire or rush the player.  When Foxy haywires, turn quickly.  If this action is failed, you will die. When rushes she will either uncloak or stay cloaked.  When charging he may also yell lines such as 'I`ve gotchya now!'")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/716354692355063818/720728710625362010/alpine_ui_plushsuit_foxy.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on Foxy the Pirate Fox:')
		embed.add_field(name="Rush Attacks", value="When he rushes and he uncloaks, you have to shock him before he disappears, or else you will lose. If he does not decloak, you don’t need to shock him. His AI is very similar to Freddy’s.")
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def animatronic_info(self, ctx):
		embed = discord.Embed(title="animatronic", colour=discord.Colour(0x64053b), description="Yarrrr, this command do be out of order lad.")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/716354692355063818/720728710625362010/alpine_ui_plushsuit_foxy.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on animatronic:')
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def animatronic_info(self, ctx):
		embed = discord.Embed(title="animatronic", colour=discord.Colour(0x64053b), description="Yarrrr, this command do be out of order lad.")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/716354692355063818/720728710625362010/alpine_ui_plushsuit_foxy.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on animatronic:')
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def toyfreddy_info(self, ctx):
		embed = discord.Embed(title="Toy Freddy", colour=discord.Colour(0x64053b), description="Toy Freddy is one of the FNaF2 animatronics. Freddy will either haywire or rush. When Toy Freddy haywires, you need to look at him with your mask on, when the Battery button becomes orange, Toy Freddy is hijacking your battery and you need to use to mask to stop it!")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/716354692355063818/720830014790303824/alpine_ui_plushsuit_toy_freddy.png")
		embed.set_footer(text="Designed by Nexus, Coded by Vyrus", icon_url='https://cdn.discordapp.com/avatars/486291212580552716/2465ea1edce2dd490b407de2b88d9094.png?size=256')
		embed.set_author(name='Helpys logs on Toy Freddy:')
		embed.add_field(name="Rush Attacks", value="When Toy Freddy rushes you, you ignore him if he doesn't uncloak, but if he decloaks, you need to Shock him!")
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def toybonnie_info(self, ctx):
		embed = discord.Embed(title="animatronic", colour=discord.Colour(0x64053b), description="Yarrrr, this command do be out of order lad.")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/716354692355063818/720728710625362010/alpine_ui_plushsuit_foxy.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on animatronic:')
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def toychica_info(self, ctx):
		embed = discord.Embed(title="animatronic", colour=discord.Colour(0x64053b), description="Yarrrr, this command do be out of order lad.")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/716354692355063818/720728710625362010/alpine_ui_plushsuit_foxy.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on animatronic:')
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def mangle_info(self, ctx):
		embed = discord.Embed(title="animatronic", colour=discord.Colour(0x64053b), description="Yarrrr, this command do be out of order lad.")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/716354692355063818/720728710625362010/alpine_ui_plushsuit_foxy.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on animatronic:')
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def balloonboy_info(self, ctx):
		embed = discord.Embed(title="animatronic", colour=discord.Colour(0x64053b), description="Yarrrr, this command do be out of order lad.")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/716354692355063818/720728710625362010/alpine_ui_plushsuit_foxy.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on animatronic:')
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def springtrap_info(self, ctx):
		embed = discord.Embed(title="Springtrap", colour=discord.Colour(0x64053b), description="Springtrap is what most consider to be the most difficult character in the game. He spawns naturally at streak 8 and above, prepare for a fight! When Springtrap haywires, his eyes will be one of two colors. If his eyes are **red**, look away quick! If his eyes are **white**, don't break eye contact! His eyes **can** change from **white to red**, but not the other way around. You'll have more time to react to his eyes changing color if you find him quickly once his haywire starts! His haywires come in chains of 2-4, be sure to listen for any movement, voice lines, or static to make sure his chain is finished. Once he starts to charge you down, make sure you deliver him a good shock once he shows himself!")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/719048697555583132/726126500663001098/alpine_ui_plushsuit_springtrap.png")
		embed.set_footer(text="Designed by Bea, Coded by Vyrus", icon_url='https://cdn.discordapp.com/avatars/159870995287638016/3205fc06c3f5abf9e82337b079b7d5dc.png?size=256')
		embed.set_author(name='Helpys logs on animatronic:')
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def toxicspringtrap_info(self, ctx):
		embed = discord.Embed(title="Toxic Springtrap", colour=discord.Colour(0x64053b), description="Toxic Springtrap is the second skin in the Wasteland series. Springtrap is what most consider to be the most difficult character in the game, prepare for a fight! When Toxic Springtrap haywires, his eyes will be one of two colors. If his eyes are **red**, look away quick! If his eyes are **white**, don't break eye contact! His eyes **can** change from **white to red**, but not the other way around. You'll have more time to react to his eyes changing color if you find him quickly once his haywire starts! His haywires come in chains of 2-4, be sure to listen for any movement, voice lines, or static to make sure his chain is finished. Once he starts to charge you down, make sure you deliver him a good shock once he shows himself!")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/716354692355063818/725836830095835207/alpine_ui_portrait_toxic_springtrap.png")
		embed.set_footer(text="Designed by Bea, Coded by Vyrus", icon_url='https://cdn.discordapp.com/avatars/159870995287638016/3205fc06c3f5abf9e82337b079b7d5dc.png?size=256')
		embed.set_author(name='Helpys logs on animatronic:')
		await ctx.message.channel.send(embed=embed)


	@commands.command()
	async def baby_info(self, ctx):
		embed = discord.Embed(title="Circus Baby", colour=discord.Colour(0x64053b), description="Yarrrr, this command do be out of order lad.")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/716354692355063818/720728710625362010/alpine_ui_plushsuit_foxy.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on Circus Baby:')
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def frostbear_info(self, ctx):
		embed = discord.Embed(title="Freddy Frostbear", colour=discord.Colour(0x64053b), description="Yarrrr, this command do be out of order lad.")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/716354692355063818/720728710625362010/alpine_ui_plushsuit_foxy.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on Freddy Frostbear:')
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def shadowbonnie_info(self, ctx):
		embed = discord.Embed(title="Shadow Bonnie", colour=discord.Colour(0x64053b), description="Yarrrr, this command do be out of order lad.")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/716354692355063818/720728710625362010/alpine_ui_plushsuit_foxy.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on Shadow Bonnie:')
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def radioactivefoxy_info(self, ctx):
		embed = discord.Embed(title="Radioactive Foxy", colour=discord.Colour(0x64053b), description="Foxy is the first of the Radioactive Skins. Like the original, he will run around you frequently until he finds an opening for an attack.  He will either haywire or rush the player.  When Foxy haywires, turn quickly.  If this action is failed, you will die. When he rushes he will either uncloak or stay cloaked.  When charging he may also yell lines such as 'I`ve gotchya now!'")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/716354692355063818/720784135848722432/alpine_ui_plushsuit_radioactive_foxy.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on Radioactive Foxy:')
		embed.add_field(name="Rush Attacks", value="When he rushes and he uncloaks, you have to shock him before he disappears, or else you will lose. If he does not decloak, you don’t need to shock him. His AI is very similar to Freddy’s.")
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def vrtoyfreddy_info(self, ctx):
		embed = discord.Embed(title="VR Toy Freddy", colour=discord.Colour(0x64053b), description="VR Toy Freddy is the first of the Arcade Mayhem Event Skins. He'll act like Toy Freddy, and either haywire or rush, except when he's on the battleground, he'll be neon orange and have the Anger of losing his VR Headset. When VR Toy Freddy haywires, you need to look at him with your mask on, when the Battery button becomes orange, VR Toy Freddy is hijacking your battery and you need to use to mask to stop it!")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/716354692355063818/720828401283366952/alpine_ui_plushsuit_vr_toyfreddy.png")
		embed.set_footer(text="Designed by Nexus, Coded by Vyrus", icon_url='https://cdn.discordapp.com/avatars/486291212580552716/2465ea1edce2dd490b407de2b88d9094.png?size=256')
		embed.set_author(name='Helpys logs on VR Toy Freddy:')
		embed.add_field(name='Rush Attack', value="When VR Toy Freddy rushes you, you ignore him if he doesn't uncloak, but if he decloaks, you need to Shock him!")
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def donate(self, ctx):
		embed=discord.Embed(title='Donate to keep me running!', description='https://paypal.me/pools/c/8pGYcXYaGa')
		embed.set_author(name='Donations')
		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def help(self, ctx):
		author = ctx.message.author

		embed = discord.Embed(
			colour = discord.Colour(0xf296ff)
)
		embed.set_author(name='Help')
		embed.add_field(name='h-hi, h-hello, h-henlo', value='Say hello to Helpy!', inline= True)
		embed.add_field(name='h-fcset (friendcode)', value='Send your friendcode into database', inline= True)
		embed.add_field(name='h-fc @user', value='Grab someones friendcode', inline= True)
		embed.add_field(name='h-animatronics', value='list of animatronics', inline= True)
		embed.add_field(name='h-(animatronicName)_info', value='Says info about animatronics', inline= True)
		embed.add_field(name='h-donate', value='Paypal Pool Link', inline= True)
		embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/716354692355063818/720712582998131281/HelpyBot.png')

		await ctx.message.channel.send(embed=embed)

	@commands.command()
	async def fireworkfreddy_info(self, ctx):
		embed = discord.Embed(title="Firework Freddy Fazbear", colour=discord.Colour(0x64053b), description="Firework Freddy is the first animatronic from the 4th of July Event. He will slowly circle the player getting closer and closer until he either haywires, or he rushes. When he haywires, you have to look away. Do not shock him. When he rushes, he will either run without uncloaking, or he will uncloak and attack you")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/660208603424358410/725834813109698600/alpine_ui_plushsuit_freddy_firework.png")
		embed.set_footer(text="Designed by Swagmcbobface, Coded by Vyrus", icon_url='https://cdn.discordapp.com/attachments/716354692355063818/720717573343281223/image0.jpg')
		embed.set_author(name='Helpys logs on Freddy Fazbear:')
		embed.add_field(name="Rush Attacks", value="When he rushes and he uncloaks, you have to shock him before he disappears, or else you will lose. If he does not decloak, you don’t need to shock him. His AI is the baseline for all characters, so remembering these tactics will help you.")
		await ctx.message.channel.send(embed=embed)
		print('Good morning USA! I have a feeling that its gonna be a wonderful day. the sun in the sky has a smile on his face, as hes a shining a salute to the american race! Oh boy its swell to say, Good Morning USA!!! GOOD MORNING USA!!!!')

	@commands.command()
	async def die(self, ctx):
		await ctx.message.channel.send(embed=discord.Embed(title="I fucking died", description='I died on June 25th 2020 from American Freddy'))
		print("Helpy fucking died")

		#FriendCode Commands

	@commands.command()
	async def fcset(self, ctx, fc=''):
		db = sqlite3.connect('HelpyBot.db')
		cursor = db.cursor()
		if fc:
			if re.search("[A-Z0-9]{10}", fc):
				if cursor.execute(f'SELECT * FROM FriendCodes WHERE UserID = {ctx.message.author.id}').fetchone():
					await ctx.message.channel.send(embed=discord.Embed(description='Helpy already has your code on file!'))
				else:
					cursor.execute('INSERT INTO FriendCodes(UserID, FriendCode) VALUES (?, ?)', (ctx.message.author.id, fc))
					db.commit()
					await ctx.message.channel.send(embed=discord.Embed(description='Helpy has carefully filed your friend code!'))
					db.close()
					cursor.close()
			else:
				await ctx.message.channel.send(embed=discord.Embed(description='Helpy did not recognize this format!'))
		else:
			await ctx.message.channel.send(embed=discord.Embed(description='Helpy can`t help with no input!'))

	@commands.command()
	async def fc(self, ctx, member: discord.Member=''):
		db = sqlite3.connect('HelpyBot.db')
		cursor = db.cursor()
		row = cursor.execute(f'SELECT * FROM FriendCodes WHERE userid = {member.id}').fetchone()
		if member:
			if row:
				await ctx.message.channel.send(embed=discord.Embed(description=row[1]))
			else:
				await ctx.message.channel.send(embed=discord.Embed(description='This person has not set their friend code!'))
		else:
			await ctx.message.channel.send(embed=discord.Embed(description='Ping someone silly!'))

	@commands.command()
	async def animatronics(self, ctx):
		embed = discord.Embed(colour = discord.Colour(0xf296ff))
		embed.set_author(name='Animatronics in FNaF AR from 06/23/2020')
		embed.add_field(name='Bare Endo', value='-Skins: None', inline= True)
		embed.add_field(name='Freddy Fazbear', value='-Skins: Shamrock Freddy. Firework Freddy', inline= True)
		embed.add_field(name='Bonnie the Bunny', value='-Skins: Chocolate Bonnie, Easter Bonnie', inline= True)
		embed.add_field(name='Chica the Chicken', value='-Skins: None', inline= True)
		embed.add_field(name='Foxy the Pirate Fox', value='-Skins: Radioactive Foxy', inline= True)
		embed.add_field(name='Circus Baby', value='-Skins: None', inline= True)
		embed.add_field(name='Springtrap', value='-Skins: Toxic Springtrap', inline= True)
		embed.add_field(name='Toy Freddy', value='-Skins: Vr Toy Freddy', inline= True)
		embed.add_field(name='Toy Chica', value='-Skins: Highscore Toy Chica', inline= True)
		embed.add_field(name='Toy Bonnie', value='-Skins: System Error Toy Bonnie', inline= True)
		embed.add_field(name='Mangle', value='-Skins: None :(', inline= True)
		embed.add_field(name='Balloon Boy', value='-Skins: None', inline= True)
		embed.add_field(name='8-bit Baby', value='-Skins: None', inline= True)
		embed.add_field(name='Frostbear', value='-Skins: None', inline= True)

		await ctx.message.channel.send(embed=embed)

def setup(client):
	client.add_cog(CommandsCog(client))
	print('Helpy.py has connected to command.py, cogs have been initiated without error!')