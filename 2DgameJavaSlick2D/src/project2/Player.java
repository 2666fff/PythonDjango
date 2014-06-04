package project2;
/* 433-294 Object Oriented Software Development
 * RPG Game Engine
 * Sample Solution
 * Author: weiqian wang<wangw>
 */

import org.newdawn.slick.Image;
import org.newdawn.slick.SlickException;

import Items.InventoryAccessory;
import Items.InventoryQuest;
import Items.InventoryWeapon;
import Items.WorldItem;
import Items.WorldQuest;
import Items.WorldWeapon;
import Monsters.Monster;

/** The character which the user plays as.
 */
public class Player extends Unit
{


    // Pixels per millisecond
    private static final double SPEED = 0.25;
    // pick up range
    private static final float pickupRange = 30;


    /** Creates a new Player.
     * @param image_path Path of player's image file.
     */
    public Player()
        throws SlickException
    {

		init(756,684);

        // Start off at (756,684)
		// Set the Player's avatar and physical size
		this.avatar = new Image("assets/units/player.png");

        this.physHeight = 37;
        this.physWidth = 47;
		//player's damage
		this.strength = 26;
	
    }

    public void init(double ix,double iy){
        this.x = ix;
        this.y = iy;
		// Give the player full health
		this.health = this.getMaxHealth();
		this.cooldown = this.icooldown;
    }
    
	public double getMaxDamage()
	{
		double damage = strength;
		
		InventoryWeapon weapon = (InventoryWeapon) (this.getInventory().hasItem("Sword of Strength"));

				
		
		// If holding a weapon
		if (weapon != null){
			damage = weapon.getMaxDamage() * (this.strength+ 100) / 100;}
		damage += this.getBonuses().get(Bonus.Type.DAMAGE);
		return damage;
	}

	public void update(World world, double dir_x, double dir_y, int delta) throws SlickException{
		// Decrease the cooldown timer if necessary
				if (this.getCooldownTimer() > 0)
				{
					this.cooldownTimer -= delta;
					// If the attack is less than half cooled down, reset rotation
					if (this.getCooldownTimer() < 0)
					{
						this.getAvatar().rotate(-this.getAvatar().getRotation());
					}
				}
		// Calculate the player's new position on successful move
		double newX = getX() + dir_x * SPEED * delta;
		double newY = getY() + dir_y * SPEED * delta;

		// Check for items near the new position
		WorldItem item = scanForItem(world);
		if (item!=null && this.getInventory().getItems().size() < 4)
		{
			this.pickupItem(item, world);
		}
		// Check for monsters near the new position
		Monster m = scanForMonster(world);
		if (m != null)
		{
			this.attack(m);
			// If the monster was killed, add xp
			if (m.getHealth() <= 0)
			{
				//monster die
				m.die(world);
			}
		}
		
		this.move(world, newX, newY, delta);	
		
		if(this.health<=0){
			this.die();
		}
	}

	/**
	 * Scan the area around the player for monsters to attack.
	 * 
	 * @param gps
	 *            The game world, which holds the list of monsters.
	 * @return The target to be attacked.
	 */
	Monster scanForMonster(World world)
	{
		// Check through every monster
		for (Monster m : world.getMonsters())
		{
			// Early failure check - if diff in either axis is too great, move
			// on
			if (Math.abs(this.getX() - m.getX()) > this.getAttackRange()
					|| Math.abs(this.getY() - m.getY()) > this.getAttackRange())
			{
				continue;
			}

			// Find the actual distance from the player
			double monsterDist = world.distanceTo(this, m);

			// If within range, return the monster as a target
			if (monsterDist <= this.getAttackRange())
			{
				return m;
			}
		}
		// No monsters in range, return null
		return null;
	}
	
	/**
	 * Converts a WorldItem to an Item and adds it to the player's inventory.
	 * 
	 * @param item
	 *            The WorldItem to be converted and added.
	 * @param world
	 *            The world from which to remove the WorldItem.
	 */
	public void pickupItem(WorldItem item, World world)
	{
		System.out.println(item.getType());
			// If it's an accessory
		if (item.getType() == Item.Type.ACCESSORY)
			{
				this.getInventory()
						.addItem(
								new InventoryAccessory(item.getName(), item.getAvatar(), item
										.getBonuses()));
				if (item.getName() == "Amulet of Vitality"){
					this.health += 40;
					this.maxHealth += 40;
				}
				else {
					this.icooldown -= 200;
				}
			}
			// If it's a weapon
			else if (item.getType() == Item.Type.WEAPON)
			{
				WorldWeapon weapon = (WorldWeapon) (item);
				this.getInventory().addItem(
						new InventoryWeapon(weapon.getName(), weapon.getAvatar(), weapon
								.getBonuses(), weapon.getMinDamage(), weapon.getMaxDamage()));
				this.strength = this.getMaxDamage();
			}
		
			// If it's a quest item
			else if (item.getType() == Item.Type.QUEST)
			{
				WorldQuest quest = (WorldQuest) (item);
				this.getInventory().addItem(
						new InventoryQuest(quest.getName(), quest.getAvatar(), quest.getBonuses()));
			}

		
		
		this.cooldown = (int) (this.icooldown + this.getBonuses().get(Bonus.Type.COOLDOWN));
		// Debug print
		System.out.println(getName() + " picked up " + item);
		// Remove the item from the world
		item.die(world);
	}

	/**
	 * Scan the area around the player for pickuppable items.
	 * 
	 * @param gps
	 *            The game world, which holds the list of world items.
	 * @return The item that may be picked up.
	 */
	WorldItem scanForItem(World world)
	{
		// Check through every WorldItem
		for (WorldItem w : world.items)
		{
			// Early failure check - if diff in either axis is too great, move
			// on
			if (Math.abs(this.getX() - w.getX()) > this.getPickupRange()
					|| Math.abs(this.getY() - w.getY()) > this.getPickupRange())
			{
				continue;
			}

			// Find the actual distance from the player
			double itemDist = world.distanceTo(this, w);

			// If within range, set the item as a pickup candidate
			if (itemDist <= pickupRange)
			{
				return w;
			}
		}
		// No items in range, return null
		return null;
	}

	/**
	 * @return the pickupRange
	 */
	public float getPickupRange()
	{
		return pickupRange;
	}
	
	/**
	 * if player die
	 */
	public void die(){
		this.init(900,590);
	}



}
