package com.artw.eyecare.receiver;

import com.artw.eyecare.service.BootService;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.widget.Toast;

public class BootReceiver extends BroadcastReceiver {

	@Override
	public void onReceive(Context context, Intent intent) {
		SharedPreferences sp = PreferenceManager.getDefaultSharedPreferences(context);
		if (sp.getBoolean("autorun", false)) {
			Intent it = new Intent(context, BootService.class);
			context.startService(it);
			Toast.makeText(context, "开机服务", 1).show();
		}
	}

}
