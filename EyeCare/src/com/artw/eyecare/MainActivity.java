package com.artw.eyecare;

import android.app.Activity;
import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.ServiceConnection;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;
import android.os.Bundle;
import android.os.IBinder;
import android.os.SystemClock;
import android.preference.PreferenceManager;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.Chronometer;
import android.widget.CompoundButton;
import android.widget.CompoundButton.OnCheckedChangeListener;
import android.widget.EditText;
import android.widget.Toast;
import android.widget.ToggleButton;

import com.artw.eyecare.service.BootService;
import com.artw.eyecare.service.BootService.mybinder;
import com.artw.eyecare.utils.ConstantSting;
import com.artw.eyecare.utils.SPUtils;

public class MainActivity extends Activity implements OnClickListener {

	myconn mc;
	private Chronometer cm_;
	public static String ACTION_UPDATEUI = "unlockfromservice";
	servReveiver broadcastReceiver ;
	private ToggleButton bt;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		Intent it = new Intent(this, BootService.class);
		startService(it);
		mc = new myconn();
		bindService(it, mc, Context.BIND_AUTO_CREATE);
		cm_ = (Chronometer) findViewById(R.id.cmt_current);
		
		EditText et_time = (EditText) findViewById(R.id.et);
		et_time.setText(SPUtils.getString(getApplicationContext()));
		bt = (ToggleButton) findViewById(R.id.bt_setAlarm);
		bt.setChecked(SPUtils.getBoolean(getApplicationContext(),ConstantSting.ALARM_ON));
		bt.setOnClickListener(this);
		
		//注册解屏接受者
		IntentFilter filter = new IntentFilter();
		filter.addAction(ACTION_UPDATEUI);
		broadcastReceiver = new servReveiver();
		registerReceiver(broadcastReceiver, filter);
		
		//开机启动勾选
		CheckBox cb_boot = (CheckBox) findViewById(R.id.cb_boot);
		SharedPreferences sp = PreferenceManager.getDefaultSharedPreferences(this);
		if(sp.getBoolean("autorun", false)){
			cb_boot.setChecked(true);
		}
		cb_boot.setOnCheckedChangeListener(new OnCheckedChangeListener() {
			
			public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
				// TODO Auto-generated method stub
				SharedPreferences spp = PreferenceManager.getDefaultSharedPreferences(MainActivity.this);
				Editor editor = spp.edit();
				editor.putBoolean("autorun", isChecked);
				editor.commit();
				SPUtils.putBoolean(getApplicationContext(),ConstantSting.ALARM_ON, true);
				bt.setChecked(true);
			}
		});
		
	}

	// Unlock broadcast from service;
	public class servReveiver extends BroadcastReceiver {

		@Override
		public void onReceive(Context arg0, Intent arg1) {
			// TODO Auto-generated method stub
			
			cm_.setBase(SystemClock.elapsedRealtime());
			cm_.start();
		}

	}

	public class myconn implements ServiceConnection {

		public void onServiceConnected(ComponentName name, IBinder service) {
			// TODO Auto-generated method stub
			long base = ((mybinder) service).getBase();
			//System.out.println("+++" + base);
			if(!SPUtils.getBoolean(getApplicationContext(), ConstantSting.FIRST_RUN)){
				cm_.setBase(SystemClock.elapsedRealtime());
				SPUtils.putBoolean(getApplicationContext(), ConstantSting.FIRST_RUN,true);
			}else{
				cm_.setBase(base);
			}
			cm_.start();
		}

		public void onServiceDisconnected(ComponentName name) {
		}

	}
	
	
	@Override
	protected void onDestroy() {
		unbindService(mc);
		unregisterReceiver(broadcastReceiver);
		super.onDestroy();
	}

	@Override
	public void onClick(View v) {
		if(bt.isChecked()){
			EditText et_time = (EditText) findViewById(R.id.et);
			String str = et_time.getText().toString().trim();
			SPUtils.putString(getApplicationContext(),str);
			Toast.makeText(getApplicationContext(), "护眼提醒开启,时间为"+str+"分钟", 1).show();
		}else{
			Toast.makeText(getApplicationContext(), "护眼提醒已关闭", 1).show();
		}
		SPUtils.putBoolean(getApplicationContext(),ConstantSting.ALARM_ON, bt.isChecked());

	}

//	@Override
//	public boolean onCreateOptionsMenu(Menu menu) {
//		// Inflate the menu; this adds items to the action bar if it is present.
//		getMenuInflater().inflate(R.menu.main, menu);
//		return true;
//	}

}
