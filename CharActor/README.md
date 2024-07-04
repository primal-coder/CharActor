# Import CharActor as ca

Importing `CharActor as ca` is just a convention. But it's a good one. It's short and sweet. Upon doing so you are granted public access to the following:

* `ca.character_bank` - The character bank will have no public attributes until you create a character.
* `ca.create` - The create function can, you guessed it, create a character. It accepts a number of parameters, but none are necessary, they are as follows; `obj_name`, `name`, `role`, `race`, `background`, `alignment` and `grid`.

## ca.create()

Creating a character is easy. You can do it in one line. But first, let's look at the parameters.

* `obj_name` - This is the identifier that will be assigned to the character. It is not necessary, but it is recommended. If you do not provide one, the character will be assigned a sequenced identifier, (e.g. `char1`, `char2`, etc.)
* `name` - The name of the character will default to 'Unnamed' if not provided.
* `role` - A string, representative of the character's role(traditionally referred to as 'class'). Will be randomly selected if not provided. The available roles are as follows:
  * 'Barbarian'
  * 'Bard'
  * 'Cleric'
  * 'Druid'
  * 'Fighter'
  * 'Monk'
  * 'Paladin'
  * 'Ranger'
  * 'Rogue'
  * 'Sorcerer'
  * 'Warlock'
  * 'Wizard'
* `race` - A string, representative of the character's race. Will be randomly selected if not provided. The available races are as follows:
  * 'Dragonborn'
  * 'Dwarf'
  * 'Elf'
  * 'Gnome'
  * 'Half-Elf'
  * 'Half-Orc'
  * 'Halfling'
  * 'Human'
  * 'Tiefling'
* `background` - A string, representative of the character's background. Will be randomly selected if not provided. The available backgrounds are as follows:
  * 'Acolyte'
  * 'Charlatan'
  * 'Criminal'
  * 'Entertainer'
  * 'Folk Hero'
  * 'Guild Artisan'
  * 'Hermit'
  * 'Noble'
  * 'Outlander'
  * 'Sage'
  * 'Sailor'
  * 'Soldier'
  * 'Urchin'
* `alignment` - A string, representative of the character's alignment. Will be randomly selected if not provided. The available alignments are as follows:
  * 'Lawful Good'
  * 'Neutral Good'
  * 'Chaotic Good'
  * 'Lawful Neutral'
  * 'Neutral'
  * 'Chaotic Neutral'
  * 'Lawful Evil'
  * 'Neutral Evil'
  * 'Chaotic Evil'

## Details

Depending on your shell, you may be able to use tab completion once you've created a character. If you're using a shell that doesn't support tab completion, you can use the `dir` function to see what attributes are available to you. Upon creating an a character instance, if you prepare a statement with the character's identifier, followed by a period, and then press tab, you will be presented with a list of attributes and methods available to you.

### ca.create() Example

```python
>>> import CharActor as ca
>>> ca.create()
>>> char1 = ca.character_bank.char1
>>> char1. # Press tab here
char1.Bard           char1.Intelligence     char1.character_sheet  char1.fortitude_save(  char1.name         char1.speed
char1.Charisma       char1.Strength         char1.dispatcher       char1.hp               char1.pickup(      char1.target
char1.Constitution   char1.Wisdom           char1.drop(            char1.initiative       char1.reflex_save( char1.will_save(
char1.Custom         char1.actions          char1.end_turn()       char1.inventory        char1.saving_throws    
char1.Dexterity      char1.age              char1.entity_id        char1.level            char1.scene            
char1.Good           char1.armor_class      char1.events           char1.look_around()    char1.skill_points     
char1.Halfling       char1.attack()         char1.experience       char1.move(            char1.skillbook 
```

Some of the attributes you will see are dynamically generated based on the parameters(see above) you provided when creating the character. For example, if you created a character with the role of 'Bard', you will see the attribute `char1.Bard`. This dynamic attribute has a static counterpart, which is always available. For example, `char1.Bard` and `char1._Role` are the same attribute. The dynamic attributes are there for convenience.

## ca.character_bank

The character bank is a dictionary of all the characters you've created. You can access it directly, but it's recommended that you use the `ca.character_bank` attribute instead. The character bank is a dictionary of character instances, with the keys being the identifiers you assigned to them. For example, if you created a character with the identifier of 'char1', you can access it by calling `ca.character_bank.char1`. You can easily assign a character to a new variable using the usual syntax. For example, `char1 = ca.character_bank.char1`.

### ca.character_bank Example

```python
>>> import CharActor as ca
>>> ca.create() # Creates a character with the identifier 'char1'
>>> char1 = ca.character_bank.char1
>>> char1.name
'Unnamed'
>>> char1.name = 'Bob'
>>> char1.name
'Bob'
```

## Using CharActor with other modules

CharActor is designed to be used in conjunction with gridengine_framework, CharObj, CharTask,  