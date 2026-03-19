deploy:
	@echo "Deploying the bot..."
	sudo cp -r ./callback_data_click_bot.service /etc/systemd/system/
	sudo systemctl daemon-reload
	sudo systemctl start callback_data_click_bot.service
	sudo systemctl enable callback_data_click_bot.service
	@echo "Bot deployed successfully."

restart:
	@echo "Restarting the bot..."
	sudo systemctl restart callback_data_click_bot.service

status:
	@echo "Checking the bot status..."
	sudo systemctl status callback_data_click_bot.service
