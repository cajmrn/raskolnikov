import discord

class EmbedTemplate:
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