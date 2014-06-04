package project2;
/*
 * Use for the bonuses provide from items to player.
 * author: weiqian wang<wangw>
 * */

import java.util.ArrayList;

public class Bonus
{
	/** All the possible bonus properties */
	public static enum Type
	{
		DAMAGE, HP, MAXHP, MP, MAXMP, SPEED, COOLDOWN, STRENGTH,
	};

	/** An empty bonus array for non-bonus item construction */
	public static final ArrayList<Bonus> EMPTY_BONUS = new ArrayList<Bonus>(0);

	/** The type of the bonus instance */
	private Bonus.Type type;
	/** The value of the bonus instance */
	private double value;

	/**
	 * Create a bonus of the given type and value
	 * 
	 * @param type
	 *            The type of bonus
	 * @param value
	 *            The value of the bonus
	 */
	public Bonus(Bonus.Type type, double value)
	{
		this.type = type;
		this.value = value;
	}

	/** Serialises the bonus for printing */
	@Override
	public String toString()
	{
		String str = this.type + ": ";
		switch (this.type)
		{
		case SPEED:
			str += "+" + (int) (this.value * 100) + "%";
			break;
		case COOLDOWN:
			str += "-" + (int) this.value;
			break;
		default:
			str += "+" + (int) this.value;
			break;
		}

		return str;
	}

	/**
	 * @return the type
	 */
	public Bonus.Type getType()
	{
		return type;
	}

	/**
	 * @return the value
	 */
	public double getValue()
	{
		return value;
	}
}
