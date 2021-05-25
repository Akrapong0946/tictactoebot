from classes import Game, Board, openingstatement
from random import choice
from discord.ext import commands
import keep_alive
import os

TOKEN = str(os.environ['TOKEN'])

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} is online!')
    
# GAME COMMANDS
firstturn = 'x'
game = Game(firstturn)

@bot.command(name='start', help='Starts TicTacToe game on the channel')
async def start_game(ctx):
    game.newgame('a')
    displayboard = game.display_board()
    await ctx.send(openingstatement)
    await ctx.send(displayboard)
    await ctx.send(f'**Player {game.turn}**, please choose a cell!')

@bot.command(name='p', help='Places an "x" or "o" in the cell at <cell_index> (square coordinates)')
async def place(ctx, cell_index):
    # assign real members to players x and o
    # sender = '{0.author.mention}'.format(ctx.message)
    # if game.players[game.firstturn] == None:
    #     game.players[game.firstturn] = sender
    # elif game.players[game.turn] == None and game.players[game.firstturn] != sender:
    #     game.players[game.turn] = sender
    # else:
    #     pass
    # await ctx.send(sender)

    list_of_cells = ('a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3')
    # !p command permission
    # if game.players[game.turn] != sender:
        # pass

    # handle cell_index input invalid
    if cell_index not in list_of_cells:
        await ctx.send(f'Cell is invalid. **Player {game.turn}**, please choose another cell!')

    # handle cell_index occupied
    elif not game.board.cell_empty(cell_index):
        await ctx.send(f'Cell is occupied. **Player {game.turn}**, please choose another cell!')

    # update board
    else:
        game.update(cell_index)
        game.nextturn()
        displayboard = game.display_board()
        await ctx.send(displayboard)

        if not game.is_over():
            choosecell_msg = choice(['your turn now!', 'please choose your cell!', 'take your pick!', 'which cell are you going with?'])
            await ctx.send(f'**Player {game.turn}**, {choosecell_msg}')

        else:
            game.nextturn()
            await ctx.send(game.end())

@bot.command(name='quit', help='Force-quits the ongoing TicTacToe game')
async def force_quit(ctx):
    game.board.clear()
    await ctx.send('**This game has ended.** See you next time!')

keep_alive.keep_alive()
bot.run(TOKEN)