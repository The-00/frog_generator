<?php
function getIp(){
	if(!empty($_SERVER['HTTP_CLIENT_IP'])){
		$ip = $_SERVER['HTTP_CLIENT_IP'];
	}elseif(!empty($_SERVER['HTTP_X_FORWARDED_FOR'])){
		$ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
	}else{
		$ip = $_SERVER['REMOTE_ADDR'];
	}
	return $ip;
}

exec("python3 /frog/generator.py 2>&1", $output);
$log  = "User: ".getIp().' - '.date("F j, Y, g:i a").PHP_EOL;
file_put_contents('/var/log/frog/log_'.date("d_m_Y").'.log', $log, FILE_APPEND);

$type = 'image/png';
header('Content-Type:'.$type);
header('Content-Disposition: filename="frog.png"');

echo base64_decode($output[0]);
?>
