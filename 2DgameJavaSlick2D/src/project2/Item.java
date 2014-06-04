package project2;
/*
 * item's ab class.
 * author: weiqian wang<wangw>
 * */
import java.util.ArrayList;


import org.newdawn.slick.Graphics;
import org.newdawn.slick.Image;


public abstract class Item
{
	/** Every different type of item */
	public static enum Type
	{
		WEAPON, ACCESSORY, CONSUMABLE, QUEST
	}

	/** The item's name */
	protected String name;
	/** The type of the item */
	protected Type type;
	/** The Image object representing the item in the world */
	protected Image avatar;
	/** A list of the bonuses applied to the item */
	protected ArrayList<Bonus> bonuses;

	/**
	 * Create an item object with optional bonuses
	 * 
	 * @param name
	 *            Name of the item
	 * @param type
	 *            Item.Type of the item
	 * @param avatar
	 *            Image representing the item
	 * @param bonuses
	 *            Bonuses to be applied to the item (null for none)
	 */
	public Item(String name, Type type, Image avatar, ArrayList<Bonus> bonuses)
	{
		this.name = name;
		this.type = type;
		this.avatar = avatar;

		// Add the bonuses
		this.bonuses = bonuses;
	}

	/**
	 * Draw the item at the given coordinates.
	 * 
	 * @param g
	 *            The graphics device to draw with
	 * @param x
	 *            The x coordinates to draw at
	 * @param y
	 *            The y coordinates to draw at
	 */
	public void render(Graphics g, float x, float y)
	{
		this.avatar.draw(x, y);
	}

	/**
	 * @return the name
	 */
	public String getName()
	{
		return name;
	}

	/**
	 * @return the avatar
	 */
	public Image getAvatar()
	{
		return avatar;
	}

	/**
	 * @return the type
	 */
	public Type getType()
	{
		return type;
	}

	/**
	 * @return the bonuses
	 */
	public ArrayList<Bonus> getBonuses()
	{
		return bonuses;
	}
}
