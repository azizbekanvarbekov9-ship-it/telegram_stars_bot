deploy:
	@echo "Deploying the bot..."
	sudo cp -r ./telegram_star_bot.service /etc/systemd/system/
	sudo systemctl daemon-reload
	sudo systemctl start telegram_star_bot.service
	sudo systemctl enable telegram_star_bot.service
	@echo "Bot deployed successfully."

restart:
	@echo "Restarting the bot..."
	sudo systemctl restart telegram_star_bot.service

status:
	@echo "Checking the bot status..."
	sudo systemctl status telegram_star_bot.service
