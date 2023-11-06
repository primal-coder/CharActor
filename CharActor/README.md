# Import CharActor as ca

Importing `CharActor as ca` is just a convention. But it's a good one. It's short and sweet. Upon doing so you are granted public access to the following:
    
* `ca.character_bank` - The character bank will have no public attributes until you create a character.
* `ca.create` - The create function can, you guessed it, create a character. It accepts a number of parameters, but none are necessary, they are as follows; `obj_name`, `name`, `role`, `race`, `background`, `alignment` and `grid`. 
  `obj_name` will designate the identifier assigned to `ca.character_bank`. 
* `ca.load_dict` - The load_dict function can be used to load one of the many json file is the `CharActor/_charactor/actor/dicts/` directory. It accepts a single parameter, `dict_name`, which is the name of the json file you wish to load.
* `ca.load_list` - See above, but for lists saved as json.
* `ca.load_dicts` - Returns a dictionary of all the json files.
* `ca.Catalogues` - Provides access to the `ca.Catalogues.get` method, which can be used to produce an Item object from either `ca.Catalogues.Goods` or `ca.Catalogues.Armory`.

## Creating a Character
Creating a character is easy. You can do it in one line. But first, let's look at the parameters.

* `obj_name` - This is the identifier that will be assigned to the character. It is not necessary, but it is recommended. If you do not provide one, the character will be assigned a sequenced identifier, (e.g. `char1`, `char2`, etc.) 
* `name` - The name of the character. Will default to 'Unnamed' if not provided.
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

#### Example

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