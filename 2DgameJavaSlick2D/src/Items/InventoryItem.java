package Items;
/*
 * items in the inventory
 * author: weiqian wang<wangw>
 * */



import java.util.ArrayList;

import org.newdawn.slick.Image;

import project2.Bonus;
import project2.Item;
import project2.Item.Type;


public class InventoryItem extends Item
{
	/**whether the item is currently equipped */
	protected boolean equipped = false;

	/**
	 * Create an inventory item object with optional bonuses
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
	public InventoryItem(String name, Type type, Image avatar, ArrayList<Bonus> bonuses)
	{
		super(name, type, avatar, bonuses);
	}
}
