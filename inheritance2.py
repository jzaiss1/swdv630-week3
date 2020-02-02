# John Zaiss (GitHub id jzaiss1)
# SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1
# Week 3 Assignment - Inheritance 2

class Spell:
  def __init__(self, incantation, name):
    self.name = name
    self.incantation = incantation

  def __str__(self):
    return self.name + ' ' + self.incantation + '\n' + self.get_description()

  def get_description(self):
    return 'No description'

  def execute(self):
    print self.incantation

class Accio(Spell):
  def __init__(self):
    Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
  def __init__(self):
    Spell.__init__(self, 'Confundo', 'Confundus Charm')

  def get_description(self):
    return 'Causes the victim to become confused and befuddled.'

def study_spell(spell):
  print spell

spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())

# Answer the following questions:

# 1. What are the parent and child classes here? The parent class is Spell.  The child classes are Accio and Confundo.

# 2. What are the base and sub-classes? The base class is Spell.  The sub-classes are are Accio and Confundo.

# 3. What is the output from this code?   Try without running if you can

    # Accio
    # Summoning Charm Accio
    # No description
    # Confundus Charm Confundo
    # Causes the victim to become confused and befuddled.

# 4. When study_spell(Confundo()) executes...what get_description method gets called and why? 
    # The get_description method in the Confundo class.  
    # It overrides the get_description parent class method.

# 5. The statement print Accio() needs to print ‘This charm summons an object to the caster, potentially over a significant distance’)? 
#    Write down the code that we need to add and/or change.

        # Add this method to the Accio class
        # def get_description(self):
        #     return 'This charm summons an object to the caster, potentially over a significant distance.'