print("\tWelcome to the Basketball Roster Program\n")
#Pedimos los nombres de los jugadores a elección del usuario
pg = input("Who is your point guard: ").title()
sg = input("Who is your shooting guard: ").title()
sf = input("Who is your small forward: ").title()
pf = input("\nWho is your power forward: ").title()
c = input("Who is your center: ").title()
#Añadimos los jugadores a una nueva lista
roster = []
roster.append(pg)
roster.append(sg)
roster.append(sf)
roster.append(pf)
roster.append(c)
print("\n\tYour starting ",len(roster)," for the upcoming basketball season")
print("\t\tPoint guard: \t\t",pg)
print("\t\tShooting guard: \t",sg)
print("\t\tSmall forward: \t\t",sf)
print("\t\tPower forward: \t\t",pf)
print("\t\tCenter: \t\t",c)
#Removemos al jugador lesionado y añadimos a uno nuevo con la variable added_player
print("\nOh no, ",sf," is injured.")
roster.remove(sf)
injured_player = sf
print("Your roster only has ",len(roster)," players.")
added_player = input(f"Who will take {injured_player}'s spot: ").title()
roster.insert(2,added_player)
#Finalmente, mostramos la lista final del equipo
print("\n\tYour starting ",len(roster)," for the upcoming basketball season")
print("\t\tPoint guard: \t\t",pg)
print("\t\tShooting guard: \t",sg)
print("\t\tSmall forward: \t\t",added_player)
print("\t\tPower forward: \t\t",pf)
print("\t\tCenter: \t\t",c)
print("\nGood Luck ",roster[2]," you will do great!")
print("Your roster now has ",len(roster)," players.")