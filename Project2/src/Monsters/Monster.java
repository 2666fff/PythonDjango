package Monsters;
/*
 * Ab class of Monsters
 * author: weiqian wang<wangw>
 * */


import org.newdawn.slick.SlickException;

import project2.Player;
import project2.Unit;
import project2.World;

public abstract class Monster extends Unit {
	/** The scan range of the monster (how close targets must be to be detected) */
	private int detectionRange = 150;
	
	/**timer for bat move*/
	private int btimer = 3000,atimer=0;
	private int[] pos = {-1,0,1};
	private double dx = 0;
	private double newX = 0;
	private double newY = 0;
	private double dy = 0;

	/**
	 * Create a new Monster object.
	 * 
	 * @param x
	 *            The x coordinate of the monster's starting position.
	 * @param y
	 *            The y coordinate of the monster's starting position.
	 * @throws SlickException
	 */
	public Monster(double x, double y) throws SlickException {
		// Set the monster's position to the spawn position given
		this.x = x;
		this.y = y;
		// Set up the monster's physical size
		this.physWidth = 34;
		this.physHeight = 44;
	}

	/**
	 * Update the player's state for a frame.
	 * 
	 * @param delta
	 *            Time passed since last frame (milliseconds).
	 * @param world
	 *            The World, which acts as a facade.
	 */
	public void update(int delta, World world) {
		// If dead, don't update
		if (health <= 0) {
			this.die(world);
			return;
		}
		// Decrease the cool down timer if necessary
		if (this.cooldownTimer > 0) {
			this.cooldownTimer -= delta;
			// If the attack is less than half cooled down, reset rotation
			if (this.getCooldownTimer() < 0) {
				this.getAvatar().rotate(-this.getAvatar().getRotation());
			}
		}

		// Attempt to find a target to attack
		Unit target = scanForTarget(world);
		if (target != null) {
			double distX = target.getX() - this.getX();
			double distY = target.getY() - this.getY();
			double distTotal = Math.sqrt(distX * distX + distY * distY);
			dx = 0;
			newX = 0;
			newY = 0;
			dy = 0;

			if (!(this instanceof PassiveMonster)) {
				// Attack and return (don't move) if the player is within
				// attacking
				// range
				if (Math.abs(distTotal) < this.attackRange) {
					this.attack(target);
					return;
				}

				dx = (distX / distTotal) * SPEED * delta;
				dy = (distY / distTotal) * SPEED * delta;
			}
			else{
				if (Math.abs(distTotal) < this.attackRange) {
					dx = (-(distX) / distTotal) * 0.2 * delta;
					dy = (-(distX) / distTotal) * 0.2 * delta;
					atimer = 0;
				}
			}
			newX = getX() + dx;
			newY = getY() + dy;
			move(world, newX, newY, delta);
			
		}
		if(btimer >0 && (this instanceof PassiveMonster) && atimer >=4999)
		{

		newX = getX() + dx;
		newY = getY() + dy;
		move(world, newX, newY, delta);
		btimer -= delta;
		
		}
		else if(btimer <=0&& (this instanceof PassiveMonster))
		{
			int index = (int)(Math.random()*3);
			dx = pos[index] * 0.2 * delta;
			index = (int)(Math.random()*3);
			dy = pos[index] * 0.2 * delta;
			btimer = 3000;
			
		}
		
		atimer += delta;
		//System.out.println(atimer);
		
	}

	/**
	 * Kills the entity, removing it from the world (called from Unit.attack())
	 * 
	 * @param world
	 *            The World to remove the entity from.
	 */
	public void die(World world) {
		// Remove the monster from the world
		world.getMonsters().remove(this);

		System.out.println(getName() + " was killed!");
	}

	/**
	 * Scan the area around the monster for targets to attack
	 * 
	 * @param world
	 *            The World, which holds the lists of units.
	 * @return The target to be attacked.
	 */
	Unit scanForTarget(World world) {
		// At present, the only target for a monster is the Player
		Player p = world.getPlayer();
		double distX = this.getX() - p.getX();
		double distY = this.getY() - p.getY();
		double playerDist = Math.sqrt(distX * distX + distY * distY);
		// If the player is within detection range, set as target
		if (playerDist < detectionRange) {
			return p;
		}
		return null;
	}

}
