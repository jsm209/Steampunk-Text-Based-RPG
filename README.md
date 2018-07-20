# Lugmere's Loss
Lugmere's Loss is a text based RPG that takes inspiration from Lovecraftian Horror, Steampunk elements, and a board game called "Eldritch Horror".

## Postmortem

(7/29/2018) I'm nearing completion of this project, just making slight balancing tweaks to the rewards in the game and making a webpage for it so I can actually show people. There are a couple things I would like my future self to know that I learned from this project:

Firstly, planning is a must. I did as much as I could to refactor, and reduce redundancies. The only thing I'm particularily proud of are the dice and name classes, but everything else is trash, especially the final encounter with The Maw. All the classes should have been no longer than like 100 lines, (maybe thats why I liked the dice and name classes; they were short!) and the writing should have been in a text file that was read in to the game. I didn't feel like dealing with delimiters, however my laziness is no excuse for better code, and it got the better of me which is disappointing.

Secondly, I have a problem with scope and motivation. What should've taken a week or two took a month, and I can't tell if that's because I felt like adding features I wanted in the game, or if I was lazy, or both. Or maybe this is just how game development works, but it took longer than I thought, which isn't something I planned for. I guess when I give time estimates, I should practically double them just to be safe.

Lastly, there was a clear gap in my knowledge when it came to certain pythonic practices. The number one thing I had trouble with is understanding why I needed to include "self" in methods, and also how to inherit such methods into other classes. Including the object itself as a parameter is weird, and I can't tell why when I try to make methods static, that it fails and gives me an error.

Overall, I purposely used as many data structures as I could (although I wished I used binary trees and dictionaries/hashmaps but eh) and I learned a lot. 
