#Acutal Bot
import os
import discord
from discord.ext import commands
from random import randrange
import keep_alive
import typing
import csv

bio_topics = []
chem_topics = []
physics_topics = []
es_topics = []
math_topics = []
energy_topics = []

def initialize():
  global bio_topics
  global chem_topics
  global physics_topics
  global es_topics
  global math_topics
  global energy_topics
  bio_topics = []
  chem_topics = []
  physics_topics = []
  es_topics = []
  math_topics = []
  energy_topics = []

  with open('topics.csv', 'r') as csvfile:
    topiclist = csv.reader(csvfile, delimiter=',')
    for row in topiclist:
      if row[0] == 'biology': 
        bio_topics.append(row[1])
      elif row[0] == 'chemistry':
        chem_topics.append(row[1])
      elif row[0] == 'physics':
        physics_topics.append(row[1])
      elif row[0] == 'earth science':
        es_topics.append(row[1])
      elif row[0] == 'math':
        math_topics.append(row[1])
      elif row[0] == 'energy': 
        energy_topics.append(row[1])
  global topics
  topics = bio_topics + chem_topics + physics_topics + es_topics + math_topics + energy_topics

initialize()


def random_topic(subject):
  chosen_topic = subject[randrange(len(subject))]
  return chosen_topic

def random_question_type():
  random_int = randrange(2)
  if random_int == 0:
    return "Multiple Choice"
  else: 
    return "Short Answer"

def short_answer_type():
  random_int = randrange(2)
  if random_int == 0:
    return "123 type"
  else: 
    return "Non-123 type"

def identify_subject(subject):
  if subject in ('biology','bio', 'b', 'Biology', 'Bio', 'B'): 
    subject = 'biology'
  elif subject in ('earth science', "Earth Science", 'ES','es'):
    subject = 'earth science'
  elif subject in ('math','Math', 'M', 'm'):
    subject = 'math'
  elif subject in ('chemistry', 'c', 'Chemistry', 'C', 'Chem', 'chem'):
    subject = 'chemistry'
  elif subject in ('energy', 'Energy', 'e', 'E'):
    subject = 'energy'
  elif subject in ('physics', 'Physics', 'p', 'P'):
    subject = 'physics'
  else: 
    subject = 'error'
  return subject

troll_message = "stahp it."

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print('Bot is ready.')

@client.command()
async def addtopic(ctx,subject,*x):
  newtopic = ' '.join(x)
  real_subject = identify_subject(subject)
  if real_subject == 'error':
    await ctx.send('Error: Subject does not exist')
  else: 
    with open('topics.csv', 'a') as csvfile:
      writer = csv.writer(csvfile, delimiter=',')
      writer.writerow([real_subject, newtopic])
    initialize()
    await ctx.send(newtopic + ' has been added to ' + subject)

@client.command(aliases=['showtopics', 'topics'])
async def showtopic(ctx):
  if topics == []:
    await ctx.send("Topic list is empty")
  output = ', '.join(topics)
  await ctx.send(output)

@client.command(aliases=['rt', 'random'])
async def randomtopic(ctx, amount: typing.Optional[int] = 1):
  if amount >=10:
    await ctx.send(troll_message)
  else:
    for x in range(amount):
      temp = random_question_type()
      temp2 = ""
      if temp == "Short Answer":
        temp2 = ", " + short_answer_type()  
      await ctx.send(random_topic(topics) + ", " + temp + temp2)

@client.command(aliases=['rb'])
async def randombio(ctx, amount: typing.Optional[int] = 1):
  if amount >=10:
    await ctx.send(troll_message)
  else:
    for x in range(amount):  
      temp = random_question_type()
      temp2 = ""
      if temp == "Short Answer":
        temp2 = ", " + short_answer_type()
      await ctx.send(random_topic(bio_topics) + ", " + temp + temp2)

@client.command(aliases=['rc'])
async def randomchem(ctx, amount: typing.Optional[int] = 1):
  if amount >=10:
    await ctx.send(troll_message)
  else:
    for x in range(amount):  
      temp = random_question_type()
      temp2 = ""
      if temp == "Short Answer":
        temp2 = ", " + short_answer_type()
      await ctx.send(random_topic(chem_topics) + ", " + temp + temp2)

@client.command(aliases=['rp'])
async def randomphysics(ctx, amount: typing.Optional[int] = 1):
  if amount >=10:
    await ctx.send(troll_message)
  else:
    for x in range(amount):  
      temp = random_question_type()
      temp2 = ""
      if temp == "Short Answer":
        temp2 = ", " + short_answer_type() 
      await ctx.send(random_topic(physics_topics) + ", " + temp + temp2)

@client.command(aliases=['res'])
async def randomearth(ctx, amount: typing.Optional[int] = 1):
  if amount >=10:
    await ctx.send(troll_message)
  else:
    for x in range(amount):  
      temp = random_question_type()
      temp2 = ""
      if temp == "Short Answer":
        temp2 = ", " + short_answer_type()
      await ctx.send(random_topic(es_topics) + ", " + temp +  temp2)

@client.command(aliases=['rm'])
async def randommath(ctx, amount: typing.Optional[int] = 1):
  if amount >=10:
    await ctx.send(troll_message)
  else:
    for x in range(amount):  
      temp = random_question_type()
      temp2 = ""
      if temp == "Short Answer":
        temp2 = ", " + short_answer_type()  
      await ctx.send(random_topic(math_topics) + ", " + temp + temp2)

@client.command(aliases=['re'])
async def randomenergy(ctx, amount: typing.Optional[int] = 1):
  if amount >=10:
    await ctx.send(troll_message)
  else:
    for x in range(amount):  
      temp = random_question_type()
      temp2 = ""
      if temp == "Short Answer":
        temp2 = ", " + short_answer_type()  
      await ctx.send(random_topic(energy_topics) + ", " + temp + temp2)

@client.command(aliases=['h'])
async def needhelp(ctx):
  await ctx.send('This is Topic Bot, where random scibowl topics can be produced.\nTheses are the commands:\n.topics - Lists all current topics\nFor commands below, add an number afterwards for the number of topics you want.\n.rb - random biology topic\n.rc - random chemistry topic\n.res - random earth science topic\n.rm - random math topic\n.re - random energy topic\n.rp - random physics topic\n.addtopic subject topic - adds a topic to the subject\n^^ subjects are: b, c, e, es, p, m for bio, chem, energy, earth science, physics, and math')

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))