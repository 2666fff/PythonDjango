package project2;
/*
 * Ab class for all units
 * author: weiqian wang<wangw>
 * */

import java.util.EnumMap;

import org.newdawn.slick.Color;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.Image;






public abstract class Unit implements GameObject {
	/** The item's position in the world */
	protected double x, y;
	/** The unit's name */
	protected String name;

	// Unit STATS
	/** 100% of the unit's health */
	protected double maxHealth = 100;
	/** The unit's current health */
	protected double health = maxHealth;
	/** The unit's strength, determines damage */
	protected double strength;
	/** The minimum time between attacks (ms) */
	protected int cooldown;
	/** The time until the next attack can be made (ms) */
	protected int cooldownTimer = 0;
	/** The minimum time between attacks (ms) */
	protected int icooldown = 600;

	/** The unit's movement speed */
	protected double SPEED = 0.25;
	/** The range in which the unit can attack enemies */
	protected int attackRange = 50;
	// RENDERING
	/** The Image object representing the object in the world */
	protected Image avatar = null;
	/** The physical width of the avatar (trimmed avatar width) */
	protected int physWidth;
	/** The physical height of the avatar (trimmed avatar height) */
	protected int physHeight;

	/** The width of the floating health bar */
	protected float healthBarWidth;
	/** The height of the floating health bar */
	protected final float healthBarHeight = 16;

	/** Whether to flip the image or not. */
	private boolean face_left = false;

	/** Mapping of types of bonuses to the unit's current value for that bonus */
	protected EnumMap<Bonus.Type, Double> bonuses;
	
	// ITEMS
	/** The inventory held by the unit */
	protected Inventory inventory = new Inventory();
	
    private double dirx;
    private double diry;

    /** Move the player in a given direction.
     * Prevents the player from moving outside the map space, and also updates
     * the direction the player is facing.
     * @param world The world the player is on (to check blocking).
     * @param dir_x The player's movement in the x axis (-1, 0 or 1).
     * @param dir_y The player's movement in the y axis (-1, 0 or 1).
     * @param delta Time passed since last frame (milliseconds).
     */
	public Unit(){
    	// Initilialise the bonuses
		this.bonuses = new EnumMap<Bonus.Type, Double>(Bonus.Type.class);
		for (Bonus.Type type : Bonus.Type.values())
		{
			this.bonuses.put(type, 0.0);
		}
	}
    public void move(World world, double newX, double newY, double delta)
    {
		// Check for collisions only if clipping is on
		//if (!noclip)
		{
			// Move the unit only if the new tile is unblocked
			if (!world.terrainBlocks(newX, this.y)
					&& !world.isUnitBlocked(this, newX, this.y))
			{
				
				// Check if the player has changed direction
				double dirX = (newX - this.getX());
				dirx = dirX;
				diry = (newY - this.getY());
				// If last move was to the left and now moving right
				if (face_left && dirX > 0)
				{
					face_left = false;
					// Set the avatar back to unflipped
					this.avatar = (this.getAvatar().getFlippedCopy(true, false));
				}
				// If last move was to the right and now moving left
				else if (!face_left && dirX < 0)
				{
					face_left = true;
					// Set the avatar back to unflipped
					this.avatar = (this.getAvatar().getFlippedCopy(true, false));
				}

				// Update position
				this.x = newX;
			}

			if (!world.terrainBlocks(this.x, newY)
					&& !world.isUnitBlocked(this, this.x, newY))
			{
				// Update position
				this.y = newY;
			}
		}
    }

	/**
	 * @return the avatar
	 */
	public Image getAvatar() {
		return avatar;
	}

	/**
	 * Render the unit in the game world, reflecting his new state.
	 * 
	 * @param g
	 *            The Slick graphics object, used for drawing.
	 */
	// @Override
	public void render(Graphics g) {
		// Draw the player at his real world co-ordinates (translated graphics)
		if (face_left) {
			this.getAvatar().draw(
					(float) (getX() - this.getAvatar().getWidth() / 2),
					(float) (getY() - this.getAvatar().getHeight() / 2));
		} else {
			this.getAvatar().draw(
					(float) getX() - this.getAvatar().getWidth() / 2,
					(float) getY() - this.getAvatar().getHeight() / 2);
		}
	}

	/**
	 * @return the x
	 */
	public double getX() {
		return x;
	}

	/**
	 * @return the y
	 */
	public double getY() {
		return y;
	}

	/**
	 * Render non-avatar details (health bar)
	 * 
	 * @param g
	 *            The graphics device to draw with
	 */
	public void renderSecondary(Graphics g) {
		if (!(this instanceof Player)) {
			renderHealthBox(g);
		}
	}

	/**
	 * Renders a floating health box above the unit with the unit's name and
	 * health representation
	 * 
	 * @param g
	 *            The graphics object to draw with.
	 */
	public void renderHealthBox(Graphics g) {
		// Colours for drawing
		// Color LABEL = new Color(0.9f, 0.9f, 0.4f); // Gold
		Color VALUE = new Color(1.0f, 1.0f, 1.0f); // White
		Color BAR_BG = new Color(0.0f, 0.0f, 0.0f, 0.8f); // Black, transp
		Color BAR = new Color(0.8f, 0.0f, 0.0f, 0.8f); // Red, transp

		// Font for drawing
		// g.setFont(world.getLabelFont());
		// Set the width of the health bar based on the unit's name
		this.healthBarWidth = Math.max(70,
				g.getFont().getWidth(this.getName()) + 6);

		// Draw the health bar
		float barX = (float) this.getX() - healthBarWidth / 2;
		float barY = (float) this.getY() - this.getPhysHeight() / 2
				- healthBarHeight - 5;

		g.setColor(BAR_BG);
		g.fillRect(barX, barY, healthBarWidth, healthBarHeight);
		g.setColor(BAR);
		g.fillRect(barX, barY,
				(healthBarWidth * ((float) getHealth() / getMaxHealth())),
				healthBarHeight);

		// Draw name text (in white)
		g.setColor(VALUE);
		float textX = barX
				+ (healthBarWidth - g.getFont().getWidth(this.getName())) / 2;
		float textY = barY
				+ (healthBarHeight - g.getFont().getHeight(this.getName())) / 2;
		g.drawString(this.getName(), textX, textY);
	}

	/**
	 * @return the maxHealth
	 */
	public int getMaxHealth() {
		return (int) (maxHealth + bonuses.get(Bonus.Type.MAXHP));
	}

	/**
	 * @return the health
	 */
	public int getHealth() {
		return (int) (health);
	}

	/**
	 * @return the bonuses
	 */
	public EnumMap<Bonus.Type, Double> getBonuses() {
		return bonuses;
	}

	/**
	 * @return the physWidth
	 */
	public int getPhysWidth() {
		return physWidth;
	}

	/**
	 * @return the physHeight
	 */
	public int getPhysHeight() {
		return physHeight;
	}

	/**
	 * @return the name
	 */
	public String getName() {
		return name;
	}

	/**
	 * @param health
	 *            the health to set
	 */
	public void setHealth(double health) {
		this.health = health;
	}

	/**
	 * @return the cooldownTimer
	 */
	public int getCooldownTimer() {
		return cooldownTimer;
	}

	/**
	 * Attack another unit, dealing damage and resetting the cooldown timer
	 * 
	 * @param target
	 *            The unit to attack
	 */
	public void attack(Unit target) {
		if (cooldownTimer <= 0) {

			// Calculate how much damage to do
			double min, max, damage;

			min = 0;
			max = this.getMaxDamage();
			damage = min + (int) (Math.random() * (max - min));

			// Deal the damage
			target.damage(damage);

			if (this.face_left) {
				this.getAvatar().rotate(-10);
			} else {
				this.getAvatar().rotate(10);
			}
			// Reduce cooldown
			this.cooldownTimer = this.cooldown;
		}
	}

	/**
	 * Gets the maximum damage done by the unit's weapon.
	 * 
	 * @return The maximum damage done by the unit's weapon
	 */
	public double getMaxDamage() {
		double damage = this.strength+ this.getBonuses().get(Bonus.Type.DAMAGE);;

		return damage;
	}

	/**
	 * Deal damage to the unit
	 * 
	 * @param damage
	 *            Amount of health to subtract
	 */
	public void damage(double damage) {
		this.health -= damage;
	}

	/**
	 * @param cooldown
	 *            the cooldown to add
	 */
	public void increaseCooldown(int cooldown)
	{
		this.cooldown += cooldown;
	}
	/**
	 * @return the attackRange
	 */
	public double getAttackRange()
	{
		return attackRange;
	}
	/**
	 * @return the inventory
	 */
	public Inventory getInventory()
	{
		return inventory;
	}
	
	/**
	 * Adjust the value of one of the unit's bonuses
	 * 
	 * @param type
	 *            The bonus to adjust
	 * @param amount
	 *            How much to adjust the bonus by
	 */
	public void adjustBonus(Bonus.Type type, double amount)
	{
		this.getBonuses().put(type, this.getBonuses().get(type) + amount);
		if (type == Bonus.Type.MAXHP && getHealth() > getMaxHealth())
		{
			setHealth(getMaxHealth());
		}
		System.out.println(getName() + " adjusted " + type + " by " + amount);
	}


	public double getdir_x(){
		return dirx;
	}
	public double getdir_y(){
		return diry;
	}


}
