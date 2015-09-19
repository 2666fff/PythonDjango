package com.artw.eyecare.receiver;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Handler;
import android.os.SystemClock;
import android.widget.Toast;

import com.artw.eyecare.service.BootService;
import com.artw.eyecare.utils.ConstantSting;
import com.artw.eyecare.utils.SPUtils;

public class UnlockReceiver extends BroadcastReceiver {

	Context ctx;

	Handler mHadler = new Handler() {
		public void handleMessage(android.os.Message msg) {
			Toast.makeText(ctx, "--ª§—€Ã·–—--", 1).show();
		};
	};

	@Override
	public void onReceive(Context context, Intent intent) {
		ctx = context;
		if (intent.getAction().equals("android.intent.action.SCREEN_ON")) {
			if (SPUtils.getBoolean(context,ConstantSting.ALARM_ON)) {
				int time = Integer.parseInt(SPUtils.getString(context));
				mHadler.sendEmptyMessageDelayed(101, time * 1000);
			}
			Toast.makeText(context, "∆¡ƒª¡¡∆", 1).show();
			Intent it = new Intent(context, BootService.class);
			it.putExtra("basetime", SystemClock.elapsedRealtime());
			it.putExtra("fromReceiver", true);
			context.startService(it);
		} else {
			mHadler.removeMessages(101);
		}

	}

}
