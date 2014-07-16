package irdc.ex06_10;


import java.io.File;
import java.io.IOException;

import android.app.Service;
import android.content.Intent;
import android.media.MediaPlayer;
import android.os.IBinder;

public class naozhong extends Service {
  private File recAudioFile;
	MediaPlayer mediaplayer =new MediaPlayer();
	private MusicPlayer mPlayer;
	@Override
	public void onCreate() {
	  String PATH_TO_FILE = "/mnt/sdcard/new.amr";  
	  //recAudioFile = new File("/mnt/sdcard", "new.amr");
    //mPlayer = new MusicPlayer(naozhong.this);
    //mPlayer.playMicFile(recAudioFile);
		//mediaplayer=MediaPlayer.create(this, R.raw.xn);
	  try
    {
      mediaplayer.setDataSource(PATH_TO_FILE);
    } catch (IllegalArgumentException e)
    {
      // TODO Auto-generated catch block
      e.printStackTrace();
    } catch (SecurityException e)
    {
      // TODO Auto-generated catch block
      e.printStackTrace();
    } catch (IllegalStateException e)
    {
      // TODO Auto-generated catch block
      e.printStackTrace();
    } catch (IOException e)
    {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
	  try
    {
      mediaplayer.prepare();
    } catch (IllegalStateException e)
    {
      // TODO Auto-generated catch block
      e.printStackTrace();
    } catch (IOException e)
    {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
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
