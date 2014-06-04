package project2;
/* 433-294 Object Oriented Software Development
 * RPG Game Engine
 * Sample Solution
 * Author:weiqian wang<wangw>
 */

import java.util.ArrayList;


import org.newdawn.slick.Color;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.Image;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.state.BasicGameState;
import org.newdawn.slick.tiled.TiledMap;

import Items.InventoryItem;
import Items.WorldAccessory;
import Items.WorldItem;
import Items.WorldWeapon;
import Items.WorldQuest;
import Monsters.AggressiveMonsters;
import Monsters.Monster;
import Monsters.PassiveMonster;
import Villagers.Garth;
import Villagers.Prince;
import Villagers.Shaman;
import Villagers.Villager;

/** Represents the entire game world.
 * (Designed to be instantiated just once for the whole game).
 */
public abstract class World extends BasicGameState
{
	/** The game's Player object */
	private static Player player;
    private TiledMap map = null;
	/** The map of the game world */
	//private Map _map;
    // Camera location, in pixels, relative to top-left of screen
    private int cam_x = 0;
    private int cam_y = 0;
    
    //panel
    Image panel;
    
	/** The villagers currently living in the game world */
	private ArrayList<Villager> villagers;
	/** The monsters the currently inhabit the World */
	private ArrayList<Monster> monsters;
	/** The items sitting around in the game world */
	public ArrayList<WorldItem> items;
   
    /** Camera X location, in pixels, relative to top-left of screen. */
    public int getCamX()
    {
        return cam_x;
    }

    /** Camera Y location, in pixels, relative to top-left of screen. */
    public int getCamY()
    {
        return cam_y;
    }

    /** Map width, in tiles. */
    public int getMapWidth()
    {
        return map.getWidth();
    }

    /** Map height, in tiles. */
    public int getMapHeight()
    {
        return map.getHeight();
    }

    /** Tile width, in pixels. */
    public int getTileWidth()
    {
        return map.getTileWidth();
    }

    /** Tile height, in pixels. */
    public int getTileHeight()
    {
        return map.getTileHeight();
    }
    

    /** Create a new World object. */
    public World()
    throws SlickException
    {
    	player = new Player();
        map = new TiledMap(RPG.ASSETS_PATH + "/map.tmx", RPG.ASSETS_PATH);
        panel = new Image("assets/panel.png");
		villagers = new ArrayList<Villager>();
		monsters = new ArrayList<Monster>();
		items = new ArrayList<WorldItem>();
		
		
		villagers.add(new Shaman(900, 540, "Elvira"));
		villagers.add(new Garth(828, 828, "Garth"));
		villagers.add(new Prince(540, 612, "Prince Aldric"));
		
		// Zombies
		monsters.add(new AggressiveMonsters(1260, 540, "Zombie"));
		monsters.add(new AggressiveMonsters(1476, 900, "Zombie"));
		monsters.add(new AggressiveMonsters(1548, 1332, "Zombie"));
		monsters.add(new AggressiveMonsters(756, 2556, "Zombie"));
		monsters.add(new AggressiveMonsters(900, 2844, "Zombie"));
		monsters.add(new AggressiveMonsters(1980, 2412, "Zombie"));
		monsters.add(new AggressiveMonsters(2844, 1548, "Zombie"));
		monsters.add(new AggressiveMonsters(2196, 1044, "Zombie"));
		monsters.add(new AggressiveMonsters(2988, 396, "Zombie"));

		// "Skeleton"
		monsters.add(new AggressiveMonsters(2916, 974, "Skeleton"));
		monsters.add(new AggressiveMonsters(1980, 612, "Skeleton"));
		monsters.add(new AggressiveMonsters(2052, 972, "Skeleton"));
		monsters.add(new AggressiveMonsters(2772, 540, "Skeleton"));

		// Bandits
		monsters.add(new AggressiveMonsters(1116, 1476, "Bandit"));
		monsters.add(new AggressiveMonsters(1260, 1908, "Bandit"));
		monsters.add(new AggressiveMonsters(540, 1476, "Bandit"));
		monsters.add(new AggressiveMonsters(1404, 2484, "Bandit"));
		monsters.add(new AggressiveMonsters(2772, 2556, "Bandit"));
		monsters.add(new AggressiveMonsters(2052, 1548, "Bandit"));
		monsters.add(new AggressiveMonsters(2052, 1404, "Bandit"));

		//NEC
		monsters.add(new AggressiveMonsters(2052, 468, "Draelic"));
		
		//Bat
		monsters.add(new PassiveMonster(1260, 540, "Bat"));
		monsters.add(new PassiveMonster(1476, 900, "Bat"));
		monsters.add(new PassiveMonster(1548, 1332, "Bat"));
		monsters.add(new PassiveMonster(756, 2556, "Bat"));
		monsters.add(new PassiveMonster(1260, 1908, "Bat"));
		monsters.add(new PassiveMonster(2772, 2556, "Bat"));
		monsters.add(new PassiveMonster(2844, 1548, "Bat"));
		monsters.add(new PassiveMonster(2196, 1044, "Bat"));
		monsters.add(new PassiveMonster(2916, 974, "Bat"));
		monsters.add(new PassiveMonster(1980, 612, "Bat"));
		monsters.add(new PassiveMonster(2052, 972, "Bat"));
		monsters.add(new PassiveMonster(2772, 540, "Bat"));
		
		
		
		// ITEMs
		ArrayList<Bonus> vitalityBonus = new ArrayList<Bonus>(1);
		vitalityBonus.add(new Bonus(Bonus.Type.MAXHP, 40));
		items.add(new WorldAccessory(972, 2916, "Amulet of Vitality", new Image(
				"assets/items/amulet.png"), vitalityBonus));
		
		ArrayList<Bonus> strengthBonus = new ArrayList<Bonus>(1);
		strengthBonus.add(new Bonus(Bonus.Type.DAMAGE, 10));
		items.add(new WorldWeapon(1980, 1476, "Sword of Strength", new Image(
				"assets/items/sword.png"), strengthBonus, 15, 30));
		
		ArrayList<Bonus> agilityBonus = new ArrayList<Bonus>(1);
		agilityBonus.add(new Bonus(Bonus.Type.COOLDOWN, 200));
		items.add(new WorldAccessory(2052, 900, "Tome of Agility", new Image(
				"assets/items/book.png"), agilityBonus));
		
		items.add(new WorldQuest(2052, 396, "Elixir of Life", new Image("assets/items/elixir.png"),
				Bonus.EMPTY_BONUS));

    }

    /** Update the game state for a frame.
     * @param dir_x The player's movement in the x axis (-1, 0 or 1).
     * @param dir_y The player's movement in the y axis (-1, 0 or 1).
     * @param delta Time passed since last frame (milliseconds).
     */
    public void update(double dir_x, double dir_y, int delta)
    throws SlickException
    {
        player.update(this, dir_x, dir_y, delta);
       // player.move(this, dir_x, dir_y, delta);

        // Update the camera based on the player's position
        cam_x = (int) player.getX() - (RPG.screenwidth/2);
        cam_y = (int) player.getY() - (RPG.screenheight/2);
        for (Villager v: villagers)
        {
        	v.update(delta, this);
        }
        for (Monster m: monsters)
        {
        	m.update(delta, this);
        }
    }

    /** Render the entire screen, so it reflects the current game state.
     * @param g The Slick graphics object, used for drawing.
     */
    public void render(Graphics g)
    throws SlickException
    {
        // Calculate the camera location (in tiles) and offset (in pixels)
        int cam_tile_x = cam_x / getTileWidth();
        int cam_offset_x = cam_x % getTileWidth();
        int cam_tile_y = cam_y / getTileHeight();
        int cam_offset_y = cam_y % getTileHeight();
        int screen_tilewidth = RPG.screenwidth / getTileWidth() + 2;    // 13
        int screen_tileheight = RPG.screenheight / getTileHeight() + 2; // 10
        map.render(-cam_offset_x, -cam_offset_y, cam_tile_x, cam_tile_y,
            screen_tilewidth, screen_tileheight);

        renderPanel(g);
		// Translate the scene to allow drawing at real co-ordinates
		g.translate((float) -this.getCameraX(), (float) -this.getCameraY());
        // Render the player
        getPlayer().render(g);
        
		// Render each villager
		for (Villager v : getVillagers())
		{
			if (isOnCamera(v))
			{
				v.render(g);
			}
		}

		// Render each villager's health and dialogue (if necessary)
		for (Villager v : getVillagers())
		{
			if (isOnCamera(v))
			{
				v.renderSecondary(g);
			}
		}
		// Render each monster
		for (Monster m : getMonsters())
		{
			if (isOnCamera(m))
			{
				m.render(g);
			}
		}

		// Render each monster's health bar
		for (Monster m : getMonsters())
		{
			if (isOnCamera(m))
			{
				m.renderSecondary(g);
			}
		}
		// Render each world item
		for (WorldItem w : items)
		{
			if (isOnCamera(w))
			{
				w.render(g);
			}
		}

		
    }

    /** Determines whether a particular map coordinate blocks movement.
     * @param x Map x coordinate (in pixels).
     * @param y Map y coordinate (in pixels).
     * @return true if the coordinate blocks movement.
     */
    public boolean terrainBlocks(double x, double y)
    {
        int tile_x = (int) x / getTileWidth();
        int tile_y = (int) y / getTileHeight();
        int tileid = map.getTileId(tile_x, tile_y, 0);
        String block = map.getTileProperty(tileid, "block", "0");
        return !block.equals("0");
    }
    
	
	/**
	 * @return the player
	 */
	public Player getPlayer()
	{
		return player;
	}
	
	/**
	 * @return the cameraX
	 */
	public double getCameraX()
	{
		return cam_x;
	}

	/**
	 * @return the cameraY
	 */
	public double getCameraY()
	{
		return cam_y;
	}

	/** Get the distance between two units */
	public double distanceTo(GameObject from, GameObject to)
	{
		// Find the distance from the player
		double distX = to.getX() - from.getX();
		double distY = to.getY() - from.getY();
		return Math.sqrt(distX * distX + distY * distY);
	}

	/**
	 * Tests whether a unit would be colliding with any other unit at given
	 * position
	 * 
	 * @param unit
	 *            The unit to test
	 * @param x
	 *            The x coord to check
	 * @param y
	 *            The y coord to check
	 * @return Whether the unit is colliding with another unit at given position
	 */
	public boolean isUnitBlocked(Unit unit, double x, double y)
	{
		// Get values of testing unit edges
		double left = x - unit.getPhysWidth() / 2;
		double right = x + unit.getPhysWidth() / 2;
		double top = y - unit.getPhysHeight() / 2;
		double bottom = y + unit.getPhysHeight() / 2;

		// Build all game units into a list for checking
		ArrayList<Unit> allUnits = new ArrayList<Unit>(getVillagers().size() + getMonsters().size());
		allUnits.add(getPlayer());
		allUnits.addAll(getMonsters());
		allUnits.addAll(getVillagers());

		// Check each unit
		for (Unit u : allUnits)
		{
			// Return false if any axes are not colliding (CST) or unit checking
			// itself
			if (left >= u.getX() + u.getPhysWidth() / 2 || right <= u.getX() - u.getPhysWidth() / 2
					|| top >= u.getY() + u.getPhysHeight() / 2
					|| bottom <= u.getY() - u.getPhysHeight() / 2 || unit.equals(u))
			{
				continue;
			}

			// Check possible collisions
			if (left < u.getX() + u.getPhysWidth() / 2 && right > u.getX() - u.getPhysWidth() / 2
					&& top < u.getY() + u.getPhysHeight() / 2
					&& bottom > u.getY() - u.getPhysHeight() / 2)
			{
				return true;
			}
		}
		return false;
	}
	
	/**
	 * 'Fall-through' method for rendering, return whether an object should be
	 * rendered.
	 * 
	 * @param obj
	 *            The WorldObject to test (Unit or WorldItem)
	 * @return whether the object is on camera (and should be rendered)
	 */
	public boolean isOnCamera(GameObject obj)
	{

		if (obj.getX() + obj.getAvatar().getWidth() / 2 > getCameraX()
				&& obj.getX() - obj.getAvatar().getWidth() / 2 < getCameraX() + RPG.screenwidth
				&& obj.getY() + obj.getAvatar().getHeight() / 2 > getCameraY()
				&& obj.getY() - obj.getAvatar().getHeight() / 2 < getCameraY() + RPG.screenheight)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	
	/**
	 * @return the Villagers
	 */
	public ArrayList<Villager> getVillagers()
	{
		return villagers;
	}
	/**
	 * @return the monsters
	 */
	public ArrayList<Monster> getMonsters()
	{
		return monsters;
	}

	
    /** Renders the player's status panel.
     * @param g The current Slick graphics context.
     */
    public void renderPanel(Graphics g)
    {
        // Panel colours
        Color LABEL = new Color(0.9f, 0.9f, 0.4f);          // Gold
        Color VALUE = new Color(1.0f, 1.0f, 1.0f);          // White
        Color BAR_BG = new Color(0.0f, 0.0f, 0.0f, 0.8f);   // Black, transp
        Color BAR = new Color(0.8f, 0.0f, 0.0f, 0.8f);      // Red, transp

        // Variables for layout
        String text;                // Text to display
        int text_x, text_y;         // Coordinates to draw text
        int bar_x, bar_y;           // Coordinates to draw rectangles
        int bar_width, bar_height;  // Size of rectangle to draw
        int hp_bar_width;           // Size of red (HP) rectangle
        int inv_x, inv_y;           // Coordinates to draw inventory item

        float health_percent;       // Player's health, as a percentage

        // Panel background image
        panel.draw(0, RPG.screenheight - RPG.panelheight);

        // Display the player's health
        text_x = 15;
        text_y = RPG.screenheight - RPG.panelheight + 25;
        g.setColor(LABEL);
        g.drawString("Health:", text_x, text_y);
        text = Integer.toString((int) player.health)+ "/"+Integer.toString((int) player.maxHealth); 
        bar_x = 90;
        bar_y = RPG.screenheight - RPG.panelheight + 20;
        bar_width = 90;
        bar_height = 30;
        health_percent =(float) (player.health/player.maxHealth);                      
        hp_bar_width = (int) (bar_width * health_percent);
        text_x = bar_x + (bar_width - g.getFont().getWidth(text)) / 2;
        g.setColor(BAR_BG);
        g.fillRect(bar_x, bar_y, bar_width, bar_height);
        g.setColor(BAR);
        g.fillRect(bar_x, bar_y, hp_bar_width, bar_height);
        g.setColor(VALUE);
        g.drawString(text, text_x, text_y);

        // Display the player's damage and cooldown
        text_x = 200;
        g.setColor(LABEL);
        g.drawString("Damage:", text_x, text_y);
        text_x += 80;
        text = Integer.toString((int) player.getMaxDamage());
        g.setColor(VALUE);
        g.drawString(text, text_x, text_y);
        text_x += 40;
        g.setColor(LABEL);
        g.drawString("Rate:", text_x, text_y);
        text_x += 55;
        text = Integer.toString((int) (player.cooldown ));
        g.setColor(VALUE);
        g.drawString(text, text_x, text_y);

        // Display the player's inventory
        g.setColor(LABEL);
        g.drawString("Items:", 420, text_y);
        bar_x = 490;
        bar_y = RPG.screenheight - RPG.panelheight + 10;
        bar_width = 288;
        bar_height = bar_height + 20;
        g.setColor(BAR_BG);
        g.fillRect(bar_x, bar_y, bar_width, bar_height);

        inv_x = 490;
        inv_y = RPG.screenheight - RPG.panelheight
            + ((RPG.panelheight - 72) / 2);
        for (InventoryItem item : player.getInventory().getItems())                // TODO
        {
        	item.render(g, inv_x, inv_y);
            inv_x += 72;
        }
    }





}
