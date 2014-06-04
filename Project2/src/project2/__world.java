package project2;
/*
 * single instance of World.
 * author: weiqian wang<wangw>
 * */

import java.util.ArrayList;

import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.state.StateBasedGame;

import Villagers.Villager;



public class __world extends World{

	public __world() throws SlickException {
		super();
		// TODO Auto-generated constructor stub
	}
	

	@Override
	public void init(GameContainer arg0, StateBasedGame arg1)
			throws SlickException {
		new ArrayList<Villager>();
	}

	@Override
	public void render(GameContainer arg0, StateBasedGame arg1, Graphics arg2)
			throws SlickException {
		super.render(arg2);
		
	}

	@Override
	public void update(double dir_x, double dir_y, int delta)
			throws SlickException {
		super.update(dir_x, dir_y, delta);
		
	}

	@Override
	public int getID() {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public void update(GameContainer arg0, StateBasedGame arg1, int arg2)
			throws SlickException {
		// TODO Auto-generated method stub
		
	}


	

	
}