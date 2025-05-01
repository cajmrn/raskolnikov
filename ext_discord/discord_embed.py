import discord

class EmbedTemplate():
    def __init__(
        self,
        title,
        color=discord.Color.blue(),
        fields=None,
        footer=None,
        thumbnail=None,
        image=None,
        author=None
    ):
        """
        Initialize an embed template.
        
        Args:
            title: The title of the embed
            color: The color of the embed (default: discord.Color.blue())
            fields: List of field dictionaries with 'name' and 'value' keys
            footer: Footer text
            thumbnail: URL for thumbnail image
            image: URL for main image
            author: Dictionary with 'name' and optionally 'url' and 'icon_url'
        """
        self.title = title
        self.color = color
        self.fields = fields or []
        self.footer = footer
        self.thumbnail = thumbnail
        self.image = image
        self.author = author

    def create_embed(self):
        """Create a discord.Embed object from the template."""
        embed = discord.Embed(title=self.title, color=self.color)
        
        # Add fields
        for field in self.fields:
            embed.add_field(name=field['name'], value=field['value'], inline=field.get('inline', True))
        
        # Add footer if exists
        if self.footer:
            embed.set_footer(text=self.footer)
            
        # Add thumbnail if exists
        if self.thumbnail:
            embed.set_thumbnail(url=self.thumbnail)
            
        # Add image if exists
        if self.image:
            embed.set_image(url=self.image)
            
        # Add author if exists
        if self.author:
            embed.set_author(
                name=self.author['name'],
                url=self.author.get('url'),
                icon_url=self.author.get('icon_url')
            )
            
        return embed
    
    @classmethod
    def get_yfinance_info(cls, ticker, res):
        """Factory for stock market embeds."""
        title = f"{res.get('shortName', ticker)} ({ticker.upper()})"
        fields = [
            {'name': 'Current Price', 'value': f"${res.get('currentPrice', 'N/A')}"},
            {'name': 'Day High', 'value': f"${res.get('dayHigh', 'N/A')}"},
            {'name': 'Day Low', 'value': f"${res.get('dayLow', 'N/A')}"},
            {'name': '52 Week High', 'value': f"${res.get('fiftyTwoWeekHigh', 'N/A')}"},
            {'name': '52 Week Low', 'value': f"${res.get('fiftyTwoWeekLow', 'N/A')}"}
        ]
        footer = f"Data from Yahoo Finance • {res.get('exchange', 'Unknown Exchange')}"
        return cls(title=title, fields=fields, footer=footer)

    @classmethod
    def get_valuation_info(cls, ticker, data):
        """Factory for valuation analysis embeds (text-only version)."""
        color = discord.Color.dark_green() if data['is_undervalued'] else discord.Color.dark_red()
        title = f"Valuation Analysis - Score: {data['total_score']}"
        
        fields = []
        for metric_name, metric_data in data['metrics'].items():
            value = metric_data['value'].item() if hasattr(metric_data['value'], 'item') else metric_data['value']
            threshold = metric_data['threshold'].item() if hasattr(metric_data.get('threshold'), 'item') else metric_data.get('threshold')
            
            formatted_value = f"{value:,.2f}" if isinstance(value, (int, float)) else str(value)
            
            status = "PASS" if metric_data['meets_criteria'] else "FAIL"
            
            fields.append({
                'name': metric_name.upper(),
                'value': (
                    f"Value: {formatted_value}\n"
                    f"Threshold: {threshold if threshold is not None else 'N/A'}\n"
                    f"Score: {metric_data['score']}/1\n"
                    f"Status: {status}"
                ),
                'inline': True
            })
        
        footer = "UNDERVALUED" if data['is_undervalued'] else "FAIRLY VALUED"
        
        return cls(
            title=title,
            color=color,
            fields=fields,
            footer=footer)