package com.artw.eyecare.utils;

import android.content.Context;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;

public class SPUtils {
	private static SharedPreferences sp;

	public static void putString(Context ctx, String time) {
		if (sp == null) {
			sp = PreferenceManager.getDefaultSharedPreferences(ctx);
		}
		sp.edit().putString(ConstantSting.ALARM_TIME, time).commit();
	}

	public static String getString(Context ctx) {
		if (sp == null) {
			sp = PreferenceManager.getDefaultSharedPreferences(ctx);
		}
		return sp.getString(ConstantSting.ALARM_TIME, "20");
	}

	public static void putBoolean(Context ctx,String key, Boolean b) {
		if (sp == null) {
			sp = PreferenceManager.getDefaultSharedPreferences(ctx);
		}
		sp.edit().putBoolean(key, b).commit();
	}
	
	public static boolean getBoolean(Context ctx,String key) {
		if (sp == null) {
			sp = PreferenceManager.getDefaultSharedPreferences(ctx);
		}
		return sp.getBoolean(key, false);
	}

}
