$mes .= qq|��ށy$m{lot}�z<br>| if $is_mobile && $m{lot};
#================================================
# �󂭂� Created by Merino
#================================================

# �󂭂��̒l�i
my $need_money = 1000;

# ���������ɓ��I���\���邩(��)
my $lot_cycle_day = 7;

my $lot_denominator = 100;

# ����܂̏ܕi
# ������ް, �ݷ�ǽ, ���ް��, ̧��ڲ�, ̫پè, ��ڲɸ��, ���ʰ�
my @wea_nos = (5,10,15,20,25,31,32);
# è�̨ݸ�, �޲��ٸ, ����ٱ��, ��ٶ���, ����ް�
my @wea_sub_nos = (4,9,14,19,24);

# �Ϻޏ܂̏ܕi
# �ޯ�޴���, �ذĴ���, �ݼުٴ���
my @egg_nos = (37,38,40);
# ��ذѴ���, ŲĴ���, ��׺�ݴ���, �޽����, Ͻ������
my @egg_sub_nos = (3,35,36,39,41);

# �߯ď܂̏ܕi
# ����ش�, ϰҲ��, ���, Ѱ, �����, �߲���, ���
my @pet_nos = (21,62,63,125,127,168,183);
# �ް�ΰ�, �ް��, �̧��, ж��, �޳�, �����, �ݼ�
my @pet_sub_nos = (7,8,17,18,64,151,184);


#================================================
# ���p����
#================================================
sub is_satisfy {
	if ($w{player} < 30) { # ��ڲ԰��30�l����
		$mes .= '����������<br>';
		&refresh;
		&n_menu;
		return 0;
	}
	return 1;
}

#================================================
sub begin {
	open my $fh, "+< $logdir/lot.cgi" or &error('�󂭂�̧�ق��J���܂���');
	eval { flock $fh, 2; };
	my $line = <$fh>;
	my($lot_next_time, $round, $atari1,$no1,$no1_sub, $atari2,$no2,$no2_sub, $atari3,$no3,$no3_sub, $atari4,$no4,$no4_sub, $atari5,$no5,$no5_sub, $next_no1,$next_no2,$next_no3,$next_no4,$next_no5, $next_no1_sub,$next_no2_sub,$next_no3_sub,$next_no4_sub,$next_no5_sub) = split /<>/, $line;
	$round++;
	$round  = $round > 9 ? 1 : $round;
	
	# ���I���\����
	if ($time > $lot_next_time) {
		# �󂭂��̌i�i�ݒ�
		$no1 = $next_no1;
		$no2 = $next_no2;
		$no3 = $next_no3;
		$no4 = $next_no4;
		$no5 = $next_no5;
		$no1_sub = $next_no1_sub;
		$no2_sub = $next_no2_sub;
		$no3_sub = $next_no3_sub;
		$no4_sub = $next_no4_sub;
		$no5_sub = $next_no5_sub;
		$next_no1 = $wea_nos[int(rand(@wea_nos))];
		$next_no2 = $egg_nos[int(rand(@egg_nos))];
		$next_no3 = int(rand(21)+20) * 10000;
		$next_no4 = $pet_nos[int(rand(@pet_nos))];
		$next_no5 = int(rand(21)+20) * 10000;
		$next_no1_sub = $wea_sub_nos[int(rand(@wea_sub_nos))];
		$next_no2_sub = $egg_sub_nos[int(rand(@egg_sub_nos))];
		$next_no3_sub = int(rand(21)+20) * 1000;
		$next_no4_sub = $pet_sub_nos[int(rand(@pet_sub_nos))];
		$next_no5_sub = int(rand(21)+20) * 1000;
		
		$lot_next_time = int($time + 24 * 3600 * $lot_cycle_day);
		$atari1 = $round . sprintf("%03d", int(rand($lot_denominator)) );
		$atari2 = $round . sprintf("%03d", int(rand($lot_denominator)) );
		$atari3 = $round . sprintf("%03d", int(rand($lot_denominator)) );
		$atari4 = $round . sprintf("%03d", int(rand($lot_denominator)) );
		$atari5 = $round . sprintf("%03d", int(rand($lot_denominator)) );
		
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh "$lot_next_time<>$round<>$atari1<>$no1<>$no1_sub<>$atari2<>$no2<>$no2_sub<>$atari3<>$no3<>$no3_sub<>$atari4<>$no4<>$no4_sub<>$atari5<>$no5<>$no5_sub<>$next_no1<>$next_no2<>$next_no3<>$next_no4<>$next_no5<>$next_no1_sub<>$next_no2_sub<>$next_no3_sub<>$next_no4_sub<>$next_no5_sub<>";
		close $fh;
		
		&write_send_news(qq|<font color="#FFCC00">�y�󂭂����I���\\�z<br>����܁y$atari1�z$weas[$no1][1] (�O��$weas[$no1_sub][1])<br>�Ϻޏ܁y$atari2�z$eggs[$no2][1] (�O��$eggs[$no2_sub][1])<br>���ݏ܁y$atari3�z$no3 G (�O��$no3_sub G)<br>�߯ď܁y$atari4�z$pets[$no4][1] (�O��$pets[$no4_sub][1])<br>��ݏ܁y$atari5�z$no5 ��� (�O��$no5_sub ���)</font>|);
	}
	close $fh;
	
	# ���I�҂�������ܕi�𑗂��
	my $mylot = $m{lot};
	if ($atari1 eq $mylot) {
		$mes .= "����!���I���߂ł�!�ܕi�� $weas[$no1][1] �͗a���菊�ɑ����Ă�������<br>";
		&send_item($m{name}, 1, $no1, $weas[$no1][4], 10, 1);
		&write_send_news(qq|$m{name}������܂ɓ��I���܂���|);
		$m{lot} = '';
	} elsif ($atari1 == $mylot - 1 || $atari1 == $mylot + 1) {
		$mes .= "�ɂ���������!���܂� $weas[$no1_sub][1] �͗a���菊�ɑ����Ă�������<br>";
		&send_item($m{name}, 1, $no1_sub, $weas[$no1_sub][4], 10, 1);
		$m{lot} = '';
	}
	if ($atari2 eq $mylot) {
		$mes .= "����!���I���߂ł�!�ܕi�� $eggs[$no2][1] �͗a���菊�ɑ����Ă�������<br>";
		&send_item($m{name}, 2, $no2, 0, 0, 1);
		&write_send_news(qq|$m{name}���Ϻޏ܂ɓ��I���܂���|);
		$m{lot} = '';
	} elsif ($atari2 == $mylot - 1 || $atari2 == $mylot + 1) {
		$mes .= "�ɂ���������!���܂� $eggs[$no2_sub][1] �͗a���菊�ɑ����Ă�������<br>";
		&send_item($m{name}, 2, $no2_sub, 0, 0, 1);
		$m{lot} = '';
	}
	if ($atari3 eq $mylot) {
		$mes .= "����!���I���߂ł�!�ܕi�� $no3 G�͑������Ă�������<br>";
		&send_money($m{name}, '�󂭂���', $no3);
		&write_send_news(qq|$m{name}�����ݏ܂ɓ��I���܂���|);
		$m{lot} = '';
	} elsif ($atari3 == $mylot - 1 || $atari3 == $mylot + 1) {
		$mes .= "�ɂ���������!���܂� $no3_sub G�͑������Ă�������<br>";
		&send_money($m{name}, '�󂭂���', $no3_sub);
		$m{lot} = '';
	}
	if ($atari4 eq $mylot) {
		$mes .= "����!���I���߂ł�!�ܕi�� $pets[$no4][1] �͗a���菊�ɑ����Ă�������<br>";
		&send_item($m{name}, 3, $no4, 0, 0, 1);
		&write_send_news(qq|$m{name}���߯ď܂ɓ��I���܂���|);
		$m{lot} = '';
	} elsif ($atari4 == $mylot - 1 || $atari4 == $mylot + 1) {
		$mes .= "�ɂ���������!���܂� $pets[$no4_sub][1] �͗a���菊�ɑ����Ă�������<br>";
		&send_item($m{name}, 3, $no4_sub, 0, 0, 1);
		$m{lot} = '';
	}
	if ($atari5 eq $mylot) {
		$mes .= "����!���I���߂ł�!�ܕi�� $no5 ��݂��������<br>";
		$m{coin} += $no5;
		&write_send_news(qq|$m{name}����ݏ܂ɓ��I���܂���|);
		$m{lot} = '';
	} elsif ($atari5 == $mylot - 1 || $atari5 == $mylot + 1) {
		$mes .= "�ɂ���������!���܂� $no5_sub ��݂��������<br>";
		$m{coin} += $no5_sub;
		$m{lot} = '';
	}
	
	my($lmin,$lhour,$lday,$lmonth) = ( localtime($lot_next_time) )[1..4];
	++$lmonth;
	
	my $round_old = $round == 1 ? 9 : $round -1;
	$mes .= qq|<font color="#FFCC00">�y��$round_old��̓��I�ԍ��z<br>����܁y$atari1�F$weas[$no1][1] (�O��$weas[$no1_sub][1])�z<br>�Ϻޏ܁y$atari2�F$eggs[$no2][1] (�O��$eggs[$no2_sub][1])�z<br>���ݏ܁y$atari3�F$no3 G (�O��$no3_sub G)�z<br>�߯ď܁y$atari4�F$pets[$no4][1] (�O��$pets[$no4_sub][1])�z<br>��ݏ܁y$atari5�F$no5 ��� (�O��$no5_sub ���)�z<br></font>|;
	$mes .= qq|<font color="#FFCCCC">�y��$round��̏ܕi�z<br>����܁y$weas[$next_no1][1] (�O��$weas[$next_no1_sub][1])�z<br>�Ϻޏ܁y$eggs[$next_no2][1] (�O��$eggs[$next_no2_sub][1])�z<br>���ݏ܁y$next_no3 G (�O��$next_no3_sub G)�z<br>�߯ď܁y$pets[$next_no4][1] (�O��$pets[$next_no4_sub][1])�z<br>��ݏ܁y$next_no5 ��� (�O��$next_no5_sub ���)�z<br></font>|;
	$mes .= "�󂭂��͂P�� $need_money G����<br>";
	$mes .= "��$round��̓��I���\\�� $lmonth��$lday��$lhour��$lmin��������<br>";
	$mes .= '�V�����̂𔃂��ꍇ�́A�������Ă��邭������������<br>' if $m{lot};
	
	&menu('��߂�', '����');
}

sub tp_1 {
	return if &is_ng_cmd(1);

	if ($m{money} >= $need_money) {
		open my $fh, "< $logdir/lot.cgi" or &error('�󂭂�̧�ق��ǂݍ��߂܂���');
		my $line = <$fh>;
		close $fh;
		my($lot_next_time, $round) = (split /<>/, $line)[0..1];
		++$round;
		$round  = $round > 9 ? 1 : $round;
		
		my($lmin,$lhour,$lday,$lmonth) = ( localtime($lot_next_time) )[1..4];
		++$lmonth;
		
		$m{lot} = $round . sprintf("%03d", int(rand($lot_denominator)) );
		$m{money} -= $need_money;
		
		$mes .= "�܂���!<br>���I���\\�� $lmonth��$lday��$lhour��$lmin��������<br>";
	}
	else {
		$mes .= "�������Ȃ���Ζ��������₵�Ȃ���<br>";
	}
	&refresh;
	$m{lib} = 'shopping';
	&n_menu;
}


1; # �폜�s��
