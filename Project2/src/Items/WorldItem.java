package Items;


/* 433-294 Object Oriented Software Development
 * world items class
 * Author: weiqian wang <wangw>
 */


import java.util.ArrayList;


import org.newdawn.slick.Graphics;
import org.newdawn.slick.Image;
import org.newdawn.slick.SlickException;

import project2.Bonus;
import project2.GameObject;
import project2.Item;
import project2.World;



public abstract class WorldItem extends Item implements GameObject
{
	/** The item's position in the world */
	protected double x, y;

	/** The physical width of the avatar (trimmed avatar width) */
	protected int physWidth;
	/** The physical height of the avatar (trimmed avatar height) */
	protected int physHeight;

	/**
	 * Create an new item in the world
	 * 
	 * @param x
	 *            The x coordinates of the starting position
	 * @param y
	 *            The y coordinates of the starting position
	 * @param name
	 *            The item's name
	 * @param avatar
	 *            The Image used to represent the item
	 * @param bonuses
	 *            The list of bonuses to be applied to the item
	 * @throws SlickException
	 */
	public WorldItem(double x, double y, String name, Type type, Image avatar,
			ArrayList<Bonus> bonuses) throws SlickException
	{
		super(name, type, avatar, bonuses);
		// Set the item's details
		this.x = x;
		this.y = y;
		this.physWidth = 25;
		this.physHeight = 30;
	}

	/**
	 * Render the object in the game world.
	 * 
	 * @param g
	 *            The Slick graphics object, used for drawing.
	 */
	public void render(Graphics g)
	{
		this.getAvatar().draw((float) (getX() - this.getAvatar().getWidth() / 2),
				(float) (getY() - this.getAvatar().getHeight() / 2));
	}

	
	/**
	 * Removes the item from the game world
	 * 
	 * @param gps
	 *            The GameplayState from which to remove the item
	 */
	public void die(World world)
	{
		world.items.remove(this);
	}

	// GETTERS
	/** @return The item x coordinate */
	public double getX()
	{
		return x;
	}

	/** @return The item y coordinate */
	public double getY()
	{
		return y;
	}

	/**
	 * @param x
	 *            the x to set
	 */
	public void setX(double x)
	{
		this.x = x;
	}

	/**
	 * @param y
	 *            the y to set
	 */
	public void setY(double y)
	{
		this.y = y;
	}

	/**
	 * @return the physWidth
	 */
	public int getPhysWidth()
	{
		return physWidth;
	}

	/**
	 * @return the physHeight
	 */
	public int getPhysHeight()
	{
		return physHeight;
	}

	public void renderSecondary(Graphics g, World world) {
		// TODO Auto-generated method stub
		
	}

}