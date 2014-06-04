package irdc.ex06_10;


import android.app.Service;
import android.content.Intent;
import android.media.MediaPlayer;
import android.os.IBinder;

public class naozhong extends Service {
	MediaPlayer mediaplayer;
	@Override
	public void onCreate() {
		
		mediaplayer=MediaPlayer.create(this, R.raw.xn);
		super.onCreate();
	}
	
  @Override
	public void onStart(Intent intent, int startId) {
		mediaplayer.start();
		super.onStart(intent, startId);
	}
	@Override
	public void onDestroy() {
		mediaplayer.stop();
		super.onDestroy();
	}

	

	@Override
	public IBinder onBind(Intent arg0) {
		// TODO Auto-generated method stub
		return null;
	}

}
