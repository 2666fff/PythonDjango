package project2;
/*
 * use for loading map
 * author: weiqian wang<wangw>
 * */
import org.newdawn.slick.tiled.TiledMap;


public abstract class Map {
	
	private TiledMap map;
	
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
}
