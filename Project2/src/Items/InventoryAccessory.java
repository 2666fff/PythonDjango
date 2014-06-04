package Items;
/*
 * Accessory in the inventory
 * author: weiqian wang<wangw>
 * */


import java.util.ArrayList;


import org.newdawn.slick.Image;

import project2.Bonus;
import project2.Item;



public class InventoryAccessory extends InventoryItem
{

	/**
	 * Create a new accessory
	 * 
	 * @param name
	 *            The name of the accessory
	 * @param avatar
	 *            The graphical representation of the accessory
	 */
	public InventoryAccessory(String name, Image avatar, ArrayList<Bonus> bonuses)
	{
		super(name, Item.Type.ACCESSORY, avatar, bonuses);
	}
}