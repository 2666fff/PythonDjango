package Items;
/*
 * weapon item in the inventory
 * author: weiqian wang<wangw>
 * */


import java.util.ArrayList;


import org.newdawn.slick.Image;

import project2.Bonus;
import project2.Item;
import project2.Item.Type;



public class InventoryWeapon extends InventoryItem
{
	/** The minimum damage the weapon can do on a successful hit */
	private double minDamage;
	/** The maximum damage the weapon can do on a successful hit */
	private double maxDamage;

	/**
	 * Create a new weapon
	 * 
	 * @param name
	 *            The name of the weapon
	 * @param avatar
	 *            The graphical representation of the weapon
	 * @param bonuses
	 *            The bonuses to be applied (if any)
	 * @param min
	 *            The weapon's minimum damage
	 * @param max
	 *            The weapon's maximum damage
	 */
	public InventoryWeapon(String name, Image avatar, ArrayList<Bonus> bonuses, double min,
			double max)
	{
		super(name, Item.Type.WEAPON, avatar, bonuses);
		this.minDamage = min;
		this.maxDamage = max;
	}


	/**
	 * @return the minDamage
	 */
	public double getMinDamage()
	{
		return minDamage;
	}

	/**
	 * @return the maxDamage
	 */
	public double getMaxDamage()
	{
		return maxDamage;
	}
}
