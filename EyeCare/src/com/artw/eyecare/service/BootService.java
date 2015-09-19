package com.artw.eyecare.service;

import com.artw.eyecare.MainActivity;
import com.artw.eyecare.MainActivity.servReveiver;
import com.artw.eyecare.receiver.UnlockReceiver;

import android.app.Service;
import android.content.BroadcastReceiver;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Binder;
import android.os.IBinder;
import android.os.SystemClock;

public class BootService extends Service {

	long basetime = 0;

	@Override
	public IBinder onBind(Intent arg0) {
		return new mybinder();
	}

	@Override
	public void onCreate() {
		UnlockReceiver ur = new UnlockReceiver();
		IntentFilter itf = new IntentFilter();
		itf.addAction("android.intent.action.SCREEN_ON");
		itf.addAction("android.intent.action.SCREEN_OFF");
		registerReceiver(ur, itf);
		super.onCreate();
	}

	@Override
	public int onStartCommand(Intent intent, int flags, int startId) {
		if (intent != null) {
			if (intent.getBooleanExtra("fromReceiver", false)) {
				basetime = intent.getLongExtra("basetime",
						SystemClock.elapsedRealtime());
				// System.out.println("receive service from broadcast == "
				// + basetime);
				Intent it = new Intent();
				it.setAction(MainActivity.ACTION_UPDATEUI);
				sendBroadcast(it);
			}

		}
		// basetime = intent.getLongExtra("basetime",
		// SystemClock.elapsedRealtime());
		return super.onStartCommand(intent, flags, startId);
	}

	public class mybinder extends Binder {
		public long getBase() {
			return basetime;
		}
	}

}
